from django.shortcuts import render
from . models import Student,Course,Class


def home(request):
    return render(request, 'home.html',{})

def student(request):
    students = Student.objects.all()
    return render(request, 'student/list.html', {'students':students})

def course(request):
    courses = Course.objects.all()
    return render(request, 'course/list.html', {'courses':courses})