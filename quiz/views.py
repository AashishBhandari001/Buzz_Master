from django.shortcuts import render
import requests
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student, Question, QuizSetting, StudentResponse, Option, Mark, Answer, StudentResult
from .serializers import StudentSerializer, QuestionSerializer, QuizSettingsSerializer, StudentResponseSerializer, StudentOptionSerializer, StudentMarkSerializer, StudentAnswerSerializer

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
            return Response({"error": "Email or Password is incorrect!"}, status=status.HTTP_401_UNAUTHORIZED)

    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_question(request):
    questions = Question.objects.all().order_by('question_id')
    options = Option.objects.all()
    marks = Mark.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    optionSerializer = StudentOptionSerializer(options, many=True)
    markSerializer = StudentMarkSerializer(marks, many=True)
    return Response({"questions": serializer.data, "options": optionSerializer.data, "marks": markSerializer.data}, status=status.HTTP_200_OK)



@api_view(['POST'])
def submit_quiz(request, student_id):
    questions_data = request.data.get('questions', [])  # Get list of questions
    results = []  # Store results for multiple questions
    grand_total_marks = 0

    try:
        student = Student.objects.filter(student_id=student_id).first()

        for question in questions_data:
            question_title = question.get('title')
            question_options = question.get('options', {})

            total_marks = 0
            counted_questions = set()  # Track unique question IDs
            answer_dict = {}

            # Fetch question details
            question_code = Question.objects.filter(title=question_title).first()
            if not question_code:
                continue  # Skip if question doesn't exist

            question_answers = Answer.objects.filter(question=question_code)
            serializer = StudentAnswerSerializer(question_answers, many=True)

            # Store correct answers in dictionary
            for answer in serializer.data:
                answer_text = answer["answer"]
                answer_dict[answer_text] = question_code.question_id


            question_id = question_code.question_id

            if question_options == answer_dict:
                mark = Mark.objects.filter(question=question_id).first()
                if mark and question_id not in counted_questions:
                    total_marks += mark.mark 
                    counted_questions.add(question_id)


            results.append({
                "title": question_title,
                "total_questions": len(answer_dict),
                "total_marks": total_marks
            })

            grand_total_marks += total_marks

        # Save Student Result in Database
        student_result = StudentResult.objects.create(
            student=student,
            total_marks=grand_total_marks
        )
        student_result.save()


        # return Response({"results": results, "grand_total_marks": grand_total_marks, "student_result_id": student_result.result_id}, status=status.HTTP_200_OK)
        return Response({"message": "Quiz Successfully submitted!"}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




def student_details(request):
    response =  requests.get('http://127.0.0.1:8000/admin/students/')
    data = response.json()
    return render(request, 'home.html', context={'data': data})

def login(request):
    return render(request, 'login.html')

