from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number', 'age', 'enrollment_date', 'created_at', 'course')
    fields = ('name', 'email', 'number', 'age', 'enrollment_date', 'course')

admin.site.register(Student, StudentAdmin)