from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    registration = models.CharField(max_length=10)
    year = models.IntegerField()
    genre = models.CharField(max_length=50)


    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=50)
    shift = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name
    
class Class(models.Model):
    name = models.CharField(max_length=50)
    student_quantity = models.IntegerField()


    def __str__(self):
        return self.name
    