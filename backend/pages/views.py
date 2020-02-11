from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request, *args, **kwargs):
    browsersList = {
        "first":"Google Chrome",
        "second":"Mozilla Firefox",
        "third":"Opera",
        "fourth":"Safari",
    }
    return render(request, 'home.html', {'browsersList': browsersList})

def about(request, *args, **kwargs):
    return render(request, 'about.html', {})

def contact(request, *args, **kwargs):
    return render(request, 'contact.html', {})