from django.shortcuts import render

# Create your views here.
# doctors/views.py
from django.shortcuts import render

def welcome(request):
    return render(request, 'app5/welcome.html')

def doc1(request):
    return render(request, 'app5/doc1.html')

def doc2(request):
    return render(request, 'app5/doc2.html')

def doc3(request):
    return render(request, 'app5/doc3.html')
