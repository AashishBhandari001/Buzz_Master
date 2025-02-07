from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Admin, Student, Question, StudentResponse, QuizSettings

class AdminUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_superuser', 'is_superadmin')
    search_fields = ('username', 'email')

admin.site.register(Admin, AdminUserAdmin)

class AdminStudent(admin.ModelAdmin):
    pass

admin.site.register(Student, AdminStudent)



class AdminQuestion(admin.ModelAdmin):
    pass

admin.site.register(Question, AdminQuestion)


class AdminQuizSettings(admin.ModelAdmin):
    pass

admin.site.register(QuizSettings, AdminQuizSettings)


class AdminStudentResponse(admin.ModelAdmin):
    pass

admin.site.register(StudentResponse, AdminStudentResponse)