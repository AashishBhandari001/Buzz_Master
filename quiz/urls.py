from django.urls import include, path
from rest_framework import routers
from .views import get_student, student_login


urlpatterns = [
    path('students/', get_student, name='get_student'),
    path('student/login/', student_login, name='student_login')
   
]

