from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Admin

class AdminUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_superuser', 'is_superadmin')
    search_fields = ('username', 'email')

admin.site.register(Admin, AdminUserAdmin)
