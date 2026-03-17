from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.home, name='home'),
    path('subject/<slug:subject_slug>/', views.subject_topics, name='subject_topics'),
    path('quiz/<slug:topic_slug>/start/', views.start_quiz, name='start_quiz'),
    path('quiz/question/', views.quiz_question, name='quiz_question'),
    path('quiz/submit/', views.submit_answer, name='submit_answer'),
    path('quiz/result/', views.quiz_result, name='quiz_result'),
    path('quiz/reset/', views.reset_quiz, name='reset_quiz'),
]
