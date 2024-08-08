from django.shortcuts import render
from .models import *
from django.http import HttpResponse,JsonResponse

# Create your views here.
def home(request):
    student=Student.objects.all()
    data={
        'students':student,
    }
    return render(request,"home.html",data)

def course(request):
    student=Student.objects.all()
    data={
        'students':student,
    }
    return render(request,"Course_details.html",data)

def register(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        age = request.POST.get('age')
        enrollment_date = request.POST.get('enrollment_date')
        course = request.POST.get('course')

        if Student.objects.filter(email=email).exists() or Student.objects.filter(number=number).exists():
            return render(request, 'studentregistration.html', {'error_message': 'Student with this email or number is already enrolled.'})

        
        student = Student(name=name,email=email,number=number,age=age,enrollment_date=enrollment_date,course=course)
        student.save()
        return render(request, 'studentregistration.html', {'sucess_message': 'Student enrolled sucessful.'})
    return render(request, 'studentregistration.html')