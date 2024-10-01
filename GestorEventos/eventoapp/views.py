from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    
    context = {
        "nombre": "Francisco",
        "edad": 44,
        "nacionalidad": "Argentino"
    }
    return render(request, 'index.html', context)

def contador(request):
    return render(request, 'contador.html')