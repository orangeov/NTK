from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse

from .forms import ProfessionalForm, StudentForm
from .models import Professional, Student

def career_view(request):
    return render(request, 'candidate/career.html', {})

def professional_create_view(request):
    if request.method == 'POST':
        form = ProfessionalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'candidate/professional_done.html', {})
    else:
        form = ProfessionalForm()
    return render(request, 'candidate/professional_create.html', {'form': form})

def student_create_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'candidate/student_done.html', {})
    else:
        form = StudentForm()
    return render(request, 'candidate/student_create.html', {'form': form})





