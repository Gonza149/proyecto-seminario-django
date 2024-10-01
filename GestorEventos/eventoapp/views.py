from django.shortcuts import render
from django.http import HttpResponse 
from .models import Feature
# Create your views here.

def index(request):
    
    




    context = {
        "nombre": "Francisco",
        "edad": 44,
        "nacionalidad": "Argentino"
    }
    return render(request, 'index.html', context)


def contador(request):

    palabras = request.POST['text'].split()
    cantidadPalabras = len(palabras)
    return render(request, 'contador.html', {"cantidad": cantidadPalabras})