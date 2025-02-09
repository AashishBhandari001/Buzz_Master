from django.urls import include, path
from rest_framework import routers
from .views import get_student, student_details

# router = routers.DefaultRouter()
# router.register(r'students', views.get_student)

urlpatterns = [
    # path('', include(router.urls)),
    path('students/', get_student, name='get_student'),
   
]

# urlpatterns += router.urls
