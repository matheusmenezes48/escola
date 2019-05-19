from django.shortcuts import render
from . models import Student,Course,Class


def home(request):
    return render(request, 'home.html',{})




def student(request):
    registration = request.GET.get('registration',None)

    if registration:
        students = Student.objects.all()

        students = students.filter(registration=registration) 
    else:
        students = Student.objects.all()

    return render(request, 'student/list.html', {'students':students})




def course(request):
     name = request.GET.get('name',None)
     if name:
        courses = Course.objects.all()
        courses = courses.filter(name__icontains=name) 
     else:
        courses = Course.objects.all()
     return render(request, 'course/list.html', {'courses':courses})

'''def course(request):
    courses = Course.objects.all()
    return render(request, 'course/list.html', {'courses':courses})'''

def classs(request):
    classs = Class.objects.all()
    return render(request, 'class/list.html', {'classs':classs})