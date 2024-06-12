from django.shortcuts import render # type: ignore
from app1.forms import inputform
def home(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            n1=data.get("input1")
            result=fact(n1)
            return render(request,"app/index.html",{'param1':result, 'param2':n1, 'form':form1})
    else:
        form1=inputform()  
    return render(request,"app/index.html",{'form':form1})
def fact(n1):
    if n1 < 0:
        return "Invalid input. Please enter a non-negative integer."
    result = 1
    if n1 == 0:
        result = 1
    else:
        for i in range(1, n1 + 1):
            result *= i
    return result















































