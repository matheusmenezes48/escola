from django.forms import ModelForm, TextInput, Select
from .models import Student
from .models import Course
from .models import Class



class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            
            'nome': TextInput(attrs={'class':'form-control',
            'placeholder': 'Exemplo: '}),
            'Matrícula': TextInput(attrs={'class':'form-control',
            'placeholder': 'Exemplo: '}),
            'Ano de nascimento': TextInput(attrs={'class':'form-control',
            'placeholder': 'Exemplo: '}),
            'Gênero': TextInput(attrs={'class':'form-control',
            'placeholder': 'Exemplo: '}),
            'turma': Select(attrs={'class':'form-control',
            'placeholder': 'Exemplo: '}),
            'course': Select(attrs={'class':'form-control',
            'placeholder': 'Exemplo: '})            
        }