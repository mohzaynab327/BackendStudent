from django.contrib import admin
from .models import Student, Course, Registration

# Register the models with the admin site
admin.site.register(Student)
admin.site.register(Course)
# admin.site.register(Registration)
