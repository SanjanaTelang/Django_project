from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {'myvar': 'sanjana '})

# def test(request):
#     return HttpResponse("<h1>this is another page</h1>")

def myData(request):
    if (request.POST):
        fname = request.POST['firstname']
        return render(request, 'output.html', {'output':fname})
    else:
        return render(request, 'index.html', {'error': 'please fill the input'})