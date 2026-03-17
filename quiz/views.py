from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.conf import settings
import google.generativeai as genai
from .models import Subject, Topic, Question


def get_ai_analysis(subject_name, topic_name, percentage):
    """AI dan test natijalari bo'yicha xulosa olish (faqat Gemini)"""
    print(f"DEBUG: AI analysis called with {subject_name}, {topic_name}, {percentage}%")
    print(f"DEBUG: GEMINI_API_KEY exists = {bool(settings.GEMINI_API_KEY)}")
    print(f"DEBUG: GEMINI_API_KEY length = {len(settings.GEMINI_API_KEY) if settings.GEMINI_API_KEY else 0}")
    
    try:
        if settings.GEMINI_API_KEY and len(settings.GEMINI_API_KEY) > 10:
            print("DEBUG: Using Gemini API")
            genai.configure(api_key=settings.GEMINI_API_KEY)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = f"Sen tajribali ustozsan. Talabaning {subject_name} fanining {topic_name} bo'yicha test natijasi {percentage} foiz bo'ldi. Unga qisqa, motivatsion va qaysi mavzularda ko'proq ishlashi kerakligi haqida professional xulosa ber. Javobing 3-4 gapdan oshmasin."
            
            response = model.generate_content(prompt)
            result = response.text.strip()
            print(f"DEBUG: Gemini response received: {result}")
            return result
        else:
            print("DEBUG: Gemini API key not found or invalid")
            return None
            
    except Exception as e:
        print(f"DEBUG: AI API error: {e}")
        import traceback
        traceback.print_exc()
        return None


def home(request):
    """Bosh sahifa - fanlar ro'yxati"""
    subjects = Subject.objects.all()
    return render(request, 'quiz/home.html', {'subjects': subjects})


def subject_topics(request, subject_slug):
    """Fanga tegishli mavzular ro'yxati"""
    subject = get_object_or_404(Subject, slug=subject_slug)
    topics = Topic.objects.filter(subject=subject).prefetch_related('questions')
    return render(request, 'quiz/topics.html', {
        'subject': subject,
        'topics': topics
    })


@login_required
def start_quiz(request, topic_slug):
    """Testni boshlash sahifasi"""
    topic = get_object_or_404(Topic, slug=topic_slug)
    questions = Question.objects.filter(topic=topic).order_by('?')
    
    if not questions.exists():
        return render(request, 'quiz/no_questions.html', {'topic': topic})
    
    request.session['quiz_data'] = {
        'topic_id': topic.id,
        'question_ids': list(questions.values_list('id', flat=True)),
        'current_question_index': 0,
        'answers': {},
        'started_at': str(request.session.get('started_at', ''))
    }
    
    return redirect('quiz:quiz_question')


@login_required
def quiz_question(request):
    """Test savollarini ko'rsatish"""
    quiz_data = request.session.get('quiz_data')
    
    if not quiz_data:
        return redirect('quiz:home')
    
    current_index = quiz_data.get('current_question_index', 0)
    question_ids = quiz_data.get('question_ids', [])
    
    if current_index >= len(question_ids):
        return redirect('quiz:quiz_result')
    
    question = get_object_or_404(Question, id=question_ids[current_index])
    total_questions = len(question_ids)
    current_number = current_index + 1
    
    return render(request, 'quiz/question.html', {
        'question': question,
        'current_number': current_number,
        'total_questions': total_questions,
        'progress': (current_number / total_questions) * 100
    })


@csrf_exempt
def submit_answer(request):
    """Javobni qabul qilish"""
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    
    quiz_data = request.session.get('quiz_data')
    if not quiz_data:
        return JsonResponse({'error': 'Quiz session not found'}, status=400)
    
    question_id = request.POST.get('question_id')
    answer = request.POST.get('answer')
    
    if not question_id or not answer:
        return JsonResponse({'error': 'Missing required data'}, status=400)
    
    question = get_object_or_404(Question, id=question_id)
    is_correct = question.check_answer(answer)
    
    quiz_data['answers'][question_id] = {
        'answer': answer,
        'is_correct': is_correct
    }
    
    quiz_data['current_question_index'] += 1
    request.session['quiz_data'] = quiz_data
    
    return JsonResponse({
        'is_correct': is_correct,
        'correct_answer': question.correct_answer,
        'has_next': quiz_data['current_question_index'] < len(quiz_data['question_ids'])
    })


@login_required
def quiz_result(request):
    """Test natijalari sahifasi"""
    quiz_data = request.session.get('quiz_data')
    
    if not quiz_data:
        return redirect('quiz:home')
    
    topic = get_object_or_404(Topic, id=quiz_data['topic_id'])
    answers = quiz_data.get('answers', {})
    
    total_questions = len(quiz_data['question_ids'])
    correct_answers = sum(1 for ans in answers.values() if ans['is_correct'])
    percentage = (correct_answers / total_questions * 100) if total_questions > 0 else 0
    
    # AI xulosasini olish
    ai_analysis = get_ai_analysis(topic.subject.name, topic.name, percentage)
    
    # Savollar va to'g'ri javoblarni olish
    questions = Question.objects.filter(id__in=quiz_data['question_ids'])
    question_results = []
    
    for question in questions:
        user_answer = answers.get(str(question.id), {})
        question_results.append({
            'question': question,
            'user_answer': user_answer.get('answer', ''),
            'is_correct': user_answer.get('is_correct', False)
        })
    
    # Sessiyani tozalash
    if 'quiz_data' in request.session:
        del request.session['quiz_data']
    
    # Progress circle uchun hisoblash
    stroke_dashoffset = 351.86 * (1 - percentage / 100)
    
    return render(request, 'quiz/result.html', {
        'topic': topic,
        'total_questions': total_questions,
        'correct_answers': correct_answers,
        'percentage': percentage,
        'question_results': question_results,
        'stroke_dashoffset': stroke_dashoffset,
        'ai_analysis': ai_analysis,
        'ai_available': bool(ai_analysis)
    })


def reset_quiz(request):
    """Testni qayta boshlash"""
    if 'quiz_data' in request.session:
        del request.session['quiz_data']
    return redirect('quiz:home')
