# app1/views.py
from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm

def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = StudentRegistrationForm()
    return render(request, 'app2/register.html', {'form': form})

def success(request):
    return render(request, 'app2/success.html')
