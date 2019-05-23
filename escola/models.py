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
    GENRER_CHOICES = (
        ('M','masculino'), ('F', 'Feminino')
    )
    name = models.CharField(max_length=50)
    registration = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    turma  = models.ForeignKey(Class, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    genrer = models.CharField(max_length=1,choices=GENRER_CHOICES)


 

    def __str__(self):
        return self.name

    