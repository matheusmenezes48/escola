from django.shortcuts import render, redirect
from . models import Student,Course,Class
from . forms import StudentForm

def home(request):
    return render(request, 'home.html',{})




def student(request):
    if request.method == "POST":
        select = request.POST.get('select')
        students = Student.objects.all().order_by(select)
        return render(request, 'student/list.html', {'students':students})
    else:
        students = Student.objects.all() 
        return render(request, 'student/list.html', {'students':students})

def student_delete(request,id):
    student = Student.objects.get(pk=id)
    form = StudentForm(request.POST, instance=student)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    else:
        student.delete()
        return redirect('student_list')

def form_student(request):
    if (request.method == 'POST'):
        form = StudentForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('/home/alunos')
        else:
            return render(request,'student/form.html',{'form':form})
    else:
        form = StudentForm()
        return render(request,'student/form.html',{'form':form})


def course(request):
     name = request.GET.get('name')
     if name:
        courses = Course.objects.all()
        courses = courses.filter(name__icontains=name) 
     else:
        courses = Course.objects.all()
     return render(request, 'course/list.html', {'courses':courses})


def classs(request):
    classs = Class.objects.all()
    return render(request, 'class/list.html', {'classs':classs})