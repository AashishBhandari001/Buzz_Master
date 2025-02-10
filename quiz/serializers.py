from rest_framework import serializers
from .models import Student, Question, QuizSetting, StudentResponse, Catogery, Option, Answer, Mark

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
        model = QuizSetting
        fields = '__all__'

class StudentResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentResponse
        fields = '__all__'

class StudentCatogerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Catogery
        fields = '__all__'


class StudentOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'

class StudentAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class StudentMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = '__all__'

