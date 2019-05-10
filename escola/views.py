from django.shortcuts import render
from . models import Student,Course,Class


def home(request):
    return render(request, 'home.html',{})