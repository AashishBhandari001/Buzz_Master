from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Admin, Student, Catogery, Question,Option, Answer, Mark , StudentResponse, QuizSetting, StudentResult

class AdminUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_superuser', 'is_superadmin')
    search_fields = ('username', 'email')

admin.site.register(Admin, AdminUserAdmin)

class AdminStudent(admin.ModelAdmin):
    list_display = ('student_id', 'full_name', 'email', 'password')
    search_fields = ('full_name', 'email')
    ordering = ['student_id']

admin.site.register(Student, AdminStudent)


class AdminQuizSettings(admin.ModelAdmin):
    list_display = ('quiz_id', 'attempt', 'duration')
    search_fields = ('quiz_id', 'duration')
    ordering = ['quiz_id']

admin.site.register(QuizSetting, AdminQuizSettings)


class AdminStudentResponse(admin.ModelAdmin):
    list_display = ('studentResponse_id', 'student', 'responses', 'submission_time')
    search_fields = ('studentResponse_id', 'student')
    ordering = ['studentResponse_id']

admin.site.register(StudentResponse, AdminStudentResponse)


class AdminStudentResult(admin.ModelAdmin):
    list_display = ('result_id', 'student', 'total_marks')
    search_fields = ('result_id', 'student')
    ordering = ['result_id']

admin.site.register(StudentResult, AdminStudentResult)


class AdminCategory(admin.ModelAdmin):
    list_display = ('catogery_id', 'name')
    search_fields = ('catogery_id', 'name')
    ordering = ['catogery_id']

admin.site.register(Catogery, AdminCategory)



class AdminOptions(admin.ModelAdmin):
    list_display = ('id','option', 'question')
    ordering = ['id']

admin.site.register(Option, AdminOptions)


class AdminAnswers(admin.ModelAdmin):
    list_display = ('id','answer', 'question')
    ordering = ['id']

admin.site.register(Answer, AdminAnswers)


class AdminMarks(admin.ModelAdmin):
    list_display = ('id','mark', 'question')
    ordering = ['id']

admin.site.register(Mark, AdminMarks)


class OptionsInlineModel(admin.TabularInline):
    model = Option
    fields = ['option']

class AnswersInlineModel(admin.TabularInline):
    model = Answer
    fields = ['answer']


class MarksInlineModel(admin.TabularInline):
    model = Mark
    fields = ['mark']


class AdminQuestion(admin.ModelAdmin):
    list_display = ('question_id', 'catogery', 'title', 'question')
    search_fields = ('question_id', 'text')
    ordering = ['question_id']
    inlines = [OptionsInlineModel, AnswersInlineModel, MarksInlineModel]

admin.site.register(Question, AdminQuestion)