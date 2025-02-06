"""
URL configuration for quiz_master project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from quiz import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/add_student/', views.add_student),
    path('admin/add_question/', views.add_question),
    path('admin/set_timer/', views.set_timer),
    path('student/submit/', views.submit_quiz),
    path('admin/export_responses/', views.export_responses),
]


admin.site.index_title = "The Quiz Master"
admin.site.site_header = "The Quiz Master Admin"
admin.site.site_title = "Site Title Quiz Master"