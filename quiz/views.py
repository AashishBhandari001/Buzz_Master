from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student, Question, QuizSettings, StudentResponse
from .serializers import StudentSerializer, QuestionSerializer, QuizSettingsSerializer, StudentResponseSerializer

@api_view(['POST'])
def add_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_question(request):
    serializer = QuestionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def set_timer(request):
    serializer = QuizSettingsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def submit_quiz(request):
    serializer = StudentResponseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Quiz submitted successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def export_responses(request):
    responses = StudentResponse.objects.all()
    serializer = StudentResponseSerializer(responses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

