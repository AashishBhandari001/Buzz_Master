from django.shortcuts import render
import requests
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student, Question, QuizSettings, StudentResponse
from .serializers import StudentSerializer, QuestionSerializer, QuizSettingsSerializer, StudentResponseSerializer

@api_view(['GET'])
def get_student(request):
    student = Student.objects.all().order_by('student_id')
    serializer = StudentSerializer(student, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def student_login(request):
    email = request.data.get('email')
    password = request.data.get('password')


    try:
        student  = Student.objects.get(email=email)

        if password == student.password:
            return Response(
                {"message": "Login Successful"}, status=status.HTTP_200_OK
            )
        else:
            return Response({"error": "Invalid credentials!"}, status=status.HTTP_401_UNAUTHORIZED)

    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_question(request):
    questions = Question.objects.all().order_by('question_id')
    serializer = QuizSettingsSerializer(questions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def submit_quiz(request):

    student_id = request.data.get('student_id')  
    responses = request.data.get('responses') 

    try:
        # Fetch student from the database
        student = Student.objects.get(student_id=student_id)

        # Check if the student has already submitted the quiz
        if StudentResponse.objects.filter(student=student).exists():
            return Response({"error": "You have already submitted the quiz!"}, status=status.HTTP_400_BAD_REQUEST)

        # Save the student response
        student_response = StudentResponse.objects.create(
            student=student,
            responses=responses
        )

        return Response(
            {"message": "Quiz submitted successfully!", "submission_id": student_response.studentResponse_id},
            status=status.HTTP_201_CREATED
        )

    except Student.DoesNotExist:
        return Response({"error": "Student not found!"}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



def student_details(request):
    response =  requests.get('http://127.0.0.1:8000/admin/students/')
    data = response.json()
    print(data)
    return render(request, 'home.html', context={'data': data})
