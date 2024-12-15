from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {'myvar': 'sanjana '})

# def test(request):
#     return HttpResponse("<h1>this is another page</h1>")

def myData(request):
    if (request.POST):
        num1 = int(request.POST["num1"])
        num2 = int(request.POST["num2"])
        result = num1 + num2
        return render(request, 'output.html', {'output':result})
    else:
        return render(request, 'index.html', {'error': 'please fill the input'})