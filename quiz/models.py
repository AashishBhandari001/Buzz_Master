from django.db import models
from django.contrib.auth.models import AbstractUser

class Admin(AbstractUser):
    """Custom Admin model inheriting from Django's AbstractUser"""
    is_superadmin = models.BooleanField(default=False)  

    def __str__(self):
        return self.username

class Student(models.Model):
    student_id = models.BigAutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(default="")
    password = models.CharField(max_length=128)


class Catogery(models.Model):
    catogery_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Question(models.Model):
    question_id = models.BigAutoField(primary_key=True)
    catogery = models.ForeignKey(Catogery, default=1, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255, verbose_name=("Title"))
    question = models.TextField(default="New Quiz")

    def __str__(self):
        return self.title

class Option(models.Model):
    option = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    

class Answer(models.Model):
    answer = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)


class Mark(models.Model):
    mark = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)

class QuizSetting(models.Model):
    quiz_id = models.BigAutoField(primary_key=True)
    attempt = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)  # Duration in minutes

class StudentResponse(models.Model):
    studentResponse_id = models.BigAutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    responses = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    submission_time = models.DateTimeField(auto_now_add=True)

class StudentResult(models.Model):
    result_id = models.BigAutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    total_marks = models.IntegerField(default=0)