from django.db import models
from django.contrib.auth.models import AbstractUser


class Admin(AbstractUser):
    """Custom Admin model inheriting from Django's AbstractUser"""
    is_superadmin = models.BooleanField(default=False)  # Extra flag for superadmins

    def __str__(self):
        return self.username

class Student(models.Model):
    symbol_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)

class Question(models.Model):
    text = models.TextField()
    options = models.JSONField()
    correct_answer = models.CharField(max_length=255, blank=True, null=True)

class QuizSettings(models.Model):
    quiz_id = models.AutoField(primary_key=True)
    duration = models.IntegerField()  # Duration in minutes

class StudentResponse(models.Model):
    symbol_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    responses = models.JSONField()
    submission_time = models.DateTimeField(auto_now_add=True)
