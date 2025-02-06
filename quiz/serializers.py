from rest_framework import serializers
from .models import Student, Question, QuizSettings, StudentResponse

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class QuizSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizSettings
        fields = '__all__'

class StudentResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentResponse
        fields = '__all__'
