from django.urls import path
from myApp.views import manage_student, manage_course,manage_registration

urlpatterns = [
    path('students/', manage_student, name='get_students'),  
    path('students/<int:id>/', manage_student, name='get_student'),
    path('course/', manage_course, name='get_course'),  
    path('course/<int:id>/', manage_course, name='get_course'), 
    path('registration/', manage_registration, name='get_registration'),
    path('registration/<int:id>/', manage_registration, name='get_registration'),
]
