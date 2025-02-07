from django.db import models
from django.contrib.auth.models import AbstractUser

class Admin(AbstractUser):
    """Custom Admin model inheriting from Django's AbstractUser"""
    is_superadmin = models.BooleanField(default=False)  # Extra flag for superadmins

    def __str__(self):
        return self.username

class Student(models.Model):
    student_id = models.BigAutoField(primary_key=True, default=0)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(default="")
    password = models.CharField(max_length=128)

class Question(models.Model):
    question_id = models.BigAutoField(primary_key=True, default=0)
    text = models.TextField(default="")
    options = models.JSONField()
    correct_answer = models.CharField(max_length=255, blank=True, null=True)

class QuizSettings(models.Model):
    quiz_id = models.BigAutoField(primary_key=True, default=0)
    attempt = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)  # Duration in minutes

class StudentResponse(models.Model):
    studentResponse_id = models.BigAutoField(primary_key=True, default=0)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    responses = models.ForeignKey(Question, on_delete=models.CASCADE)
    submission_time = models.DateTimeField(auto_now_add=True)

class StudentResult(models.Model):
    result_id = models.BigAutoField(primary_key=True, default=0)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    total_marks = models.IntegerField(default=0)