from django import forms

from .models import Professional, Student


class FileInput(forms.FileInput):
	input_type = 'file'

class EmailInput(forms.EmailInput):
	input_type = 'email'

class TextInput(forms.TextInput):
	input_type = 'textarea'

class DateInput(forms.DateInput):
	input_type = 'date'

class Select(forms.Select):
	input_type = 'select'

class ProfessionalForm(forms.ModelForm):
    class Meta:
        model = Professional
        fields = [
        'last_name',
        'first_name',
        'middle_name',
        'date_birth',
        'gender',
        'email',
        'telephone',
        'type_education',
        'program',
        'qualification',
        'address',
        'ready_to_move',
        'work_type',
        'work_post',
        'upload',
        
        ]
        widgets = {
        'gender': Select(attrs={'class': 'custom-select d-block w-100'}),
        'date_birth': DateInput(attrs={'type': 'date','class': 'form-control', 'value':'2020-01-01'}),
		'last_name': TextInput(attrs={'class': 'form-control', 'autofocus':''}),
		'first_name': TextInput(attrs={'class': 'form-control'}),
		'middle_name': TextInput(attrs={'class': 'form-control'}),
		'email': EmailInput(attrs={'class': 'form-control'}),
		'telephone': TextInput(attrs={'class': 'form-control', 'value':'+7'}),
		'type_education': Select(attrs={'class': 'custom-select'}),
		'program': TextInput(attrs={'class': 'form-control'}),
		'qualification': TextInput(attrs={'class': 'form-control'}),
		'address': TextInput(attrs={'class': 'form-control'}),
		'ready_to_move': Select(attrs={'class': 'custom-select'}),
		'work_type': Select(attrs={'class': 'custom-select d-block w-100'}),
		'work_post': TextInput(attrs={'class': 'form-control'}),
        'upload': FileInput(attrs={'class': 'form-control'}),

        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
        'last_name',
        'first_name',
        'middle_name',
        'date_birth',
        'email',
        'telephone',
        'gender',
        'praktika',
        'university', 
        'institute', 
        'specialty', 
        'year_of_begin', 
        'year_of_end',
        
        ]
        widgets = {
        'gender': Select(attrs={'class': 'custom-select d-block w-100'}),
        'date_birth': DateInput(attrs={'type': 'date','class': 'form-control', 'value':'2020-01-01'}),
        'last_name': TextInput(attrs={'class': 'form-control', 'autofocus':''}),
        'first_name': TextInput(attrs={'class': 'form-control'}),
        'middle_name': TextInput(attrs={'class': 'form-control'}),
        'email': EmailInput(attrs={'class': 'form-control'}),
        'telephone': TextInput(attrs={'class': 'form-control', 'value':'+7'}),
        'praktika': Select(attrs={'class': 'custom-select d-block w-100'}),
        'university': TextInput(attrs={'class': 'form-control'}),
        'institute': TextInput(attrs={'class': 'form-control'}),
        'specialty': TextInput(attrs={'class': 'form-control'}),
        'year_of_begin': TextInput(attrs={'class': 'form-control'}),
        'year_of_end': TextInput(attrs={'class': 'form-control'}),

        }