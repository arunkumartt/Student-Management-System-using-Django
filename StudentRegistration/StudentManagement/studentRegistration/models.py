from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50, default='name')
    email = models.EmailField(max_length=500, default='email')
    number = models.BigIntegerField(default=10)
    age=models.IntegerField(default=0)
    enrollment_date=models.DateField()
    COURSE_CHOICES = [
        ('python', 'Python'),
        ('php', 'PHP'),
    ]
    course = models.CharField(max_length=10, choices=COURSE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)