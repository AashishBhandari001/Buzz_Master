from django.urls import include, path
from rest_framework import routers
from .views import get_student, get_question, student_login, submit_quiz


urlpatterns = [
    path('students/', get_student, name='get_student'),
    path('student/question/', get_question, name='get_question'),
    path('student/login/', student_login, name='student_login'),
    path('student_response/<int:student_id>/', submit_quiz, name='submit')
   
]

