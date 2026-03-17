from django.core.management.base import BaseCommand
from quiz.models import Subject, Topic, Question


class Command(BaseCommand):
    help = 'Create sample data for testing the quiz application'

    def handle(self, *args, **options):
        # Create subjects
        subjects_data = [
            {'name': 'Matematika', 'slug': 'matematika'},
            {'name': 'Fizika', 'slug': 'fizika'},
            {'name': 'Informatika', 'slug': 'informatika'},
        ]

        for subject_data in subjects_data:
            subject, created = Subject.objects.get_or_create(
                slug=subject_data['slug'],
                defaults={'name': subject_data['name']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created subject: {subject.name}"))

        # Create topics and questions
        topics_questions = {
            'matematika': [
                {
                    'name': 'Algebra',
                    'slug': 'algebra',
                    'questions': [
                        {
                            'question_text': '2x + 5 = 15 tenglamada x ning qiymatini toping.',
                            'option_a': 'x = 5',
                            'option_b': 'x = 10',
                            'option_c': 'x = 7.5',
                            'option_d': 'x = 2.5',
                            'correct_answer': 'a'
                        },
                        {
                            'question_text': '3² + 4² = ?',
                            'option_a': '12',
                            'option_b': '25',
                            'option_c': '49',
                            'option_d': '7',
                            'correct_answer': 'b'
                        },
                        {
                            'question_text': '(x + 3)(x - 2) ko\'paytmasini yoying.',
                            'option_a': 'x² + x - 6',
                            'option_b': 'x² - x - 6',
                            'option_c': 'x² + x + 6',
                            'option_d': 'x² - x + 6',
                            'correct_answer': 'a'
                        }
                    ]
                },
                {
                    'name': 'Geometriya',
                    'slug': 'geometriya',
                    'questions': [
                        {
                            'question_text': 'Kvadratning perimetri 20 cm bo\'lsa, uning tomoni necha cm?',
                            'option_a': '4 cm',
                            'option_b': '5 cm',
                            'option_c': '10 cm',
                            'option_d': '20 cm',
                            'correct_answer': 'b'
                        },
                        {
                            'question_text': 'Aylana radiusi 7 cm bo\'lsa, uning yuzi nimaga teng? (π = 22/7)',
                            'option_a': '44 cm²',
                            'option_b': '154 cm²',
                            'option_c': '22 cm²',
                            'option_d': '308 cm²',
                            'correct_answer': 'b'
                        }
                    ]
                }
            ],
            'fizika': [
                {
                    'name': 'Mexanika',
                    'slug': 'mexanika',
                    'questions': [
                        {
                            'question_text': 'Jismning massasi 2 kg, tezligi 3 m/s bo\'lsa, uning kinetik energiyasi qancha?',
                            'option_a': '6 J',
                            'option_b': '9 J',
                            'option_c': '12 J',
                            'option_d': '18 J',
                            'correct_answer': 'b'
                        },
                        {
                            'question_text': 'Guruhning tezligi 10 m/s, vaqt 5 sekund bo\'lsa, bosib o\'tgan yo\'l qancha?',
                            'option_a': '2 m',
                            'option_b': '15 m',
                            'option_c': '50 m',
                            'option_d': '0.5 m',
                            'correct_answer': 'c'
                        }
                    ]
                }
            ],
            'informatika': [
                {
                    'name': 'Dasturlash asoslari',
                    'slug': 'dasturlash-asoslari',
                    'questions': [
                        {
                            'question_text': 'Python dasturlash tilida "print" funksiyasi qanday ishlaydi?',
                            'option_a': 'Ma\'lumotlarni input qiladi',
                            'option_b': 'Ma\'lumotlarni ekranga chiqaradi',
                            'option_c': 'Hisoblash amallarini bajaradi',
                            'option_d': 'Fayllarni saqlaydi',
                            'correct_answer': 'b'
                        },
                        {
                            'question_text': 'Quyidagilardan qaysi biri ma\'lumot turlariga tegishli emas?',
                            'option_a': 'int',
                            'option_b': 'str',
                            'option_c': 'for',
                            'option_d': 'float',
                            'correct_answer': 'c'
                        },
                        {
                            'question_text': 'List (ro\'yxat) elementlariga qanday murojaat qilinadi?',
                            'option_a': 'Fazilat (.) orqali',
                            'option_b': 'Indeks [] orqali',
                            'option_c': 'Qavslar () orqali',
                            'option_d': 'Teglash orqali',
                            'correct_answer': 'b'
                        }
                    ]
                },
                {
                    'name': 'Algoritmlar',
                    'slug': 'algoritmlar',
                    'questions': [
                        {
                            'question_text': 'Bubble sort algoritmining murakkabligi qanday?',
                            'option_a': 'O(n)',
                            'option_b': 'O(n log n)',
                            'option_c': 'O(n²)',
                            'option_d': 'O(log n)',
                            'correct_answer': 'c'
                        },
                        {
                            'question_text': 'Binary search qanday shartda ishlaydi?',
                            'option_a': 'Tartibsiz massivda',
                            'option_b': 'Tartiblangan massivda',
                            'option_c': 'Har qanday massivda',
                            'option_d': 'Faqat stringlarda',
                            'correct_answer': 'b'
                        }
                    ]
                }
            ]
        }

        # Create topics and questions
        for subject_slug, topics_data in topics_questions.items():
            subject = Subject.objects.get(slug=subject_slug)
            
            for topic_data in topics_data:
                topic, created = Topic.objects.get_or_create(
                    slug=topic_data['slug'],
                    subject=subject,
                    defaults={'name': topic_data['name']}
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Created topic: {topic.name}"))

                # Create questions
                for question_data in topic_data['questions']:
                    question, created = Question.objects.get_or_create(
                        topic=topic,
                        question_text=question_data['question_text'],
                        defaults={
                            'option_a': question_data['option_a'],
                            'option_b': question_data['option_b'],
                            'option_c': question_data['option_c'],
                            'option_d': question_data['option_d'],
                            'correct_answer': question_data['correct_answer']
                        }
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f"Created question: {question.question_text[:50]}..."))

        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))
