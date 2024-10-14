from django.shortcuts import render
from django.http import HttpResponse 
from .models import Feature

from .forms import FeatureForm
# Create your views here.

def index(request):
    context = {}
    formulario = FeatureForm()
    features = Feature.objects.all()

    context['features'] = features
    context['formulario'] = formulario

    return render(request, 'index.html', context)

def contador(request):

    palabras = request.POST['text'].split()
    cantidadPalabras = len(palabras)
    return render(request, 'contador.html', {"cantidad": cantidadPalabras})