from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('alunos/',views.student,name='student_list'),
    path('alunos/delete/<int:id>/',views.student_delete),
    path('courses/',views.course),
    path('classs/',views.classs),
    path('alunos/form/',views.form_student)


    
]
