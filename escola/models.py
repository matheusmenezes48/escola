from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=50)
    modality = models.CharField(max_length=50)
    shift = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Class(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=50)
    registration = models.CharField(max_length=10)
    year = models.IntegerField()
    genre = models.CharField(max_length=50)
    turma  = models.ForeignKey(Class, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    