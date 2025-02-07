from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    max_student = models.IntegerField()
    course_code = models.CharField(max_length=30)

    def __str__(self):
        return self.name  # You should return the name or something unique

class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='registrations')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='registrations')
    registration_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'pending'), ('approved', 'approved'), ('rejected', 'rejected')],
        default='pending'
    )

    def __str__(self):
        return f'{self.student.name} registered for {self.course.name}'
