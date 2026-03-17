from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from .models import Subject, Topic, Question


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
    
    return render(request, 'quiz/result.html', {
        'topic': topic,
        'total_questions': total_questions,
        'correct_answers': correct_answers,
        'percentage': percentage,
        'question_results': question_results
    })


def reset_quiz(request):
    """Testni qayta boshlash"""
    if 'quiz_data' in request.session:
        del request.session['quiz_data']
    return redirect('quiz:home')
