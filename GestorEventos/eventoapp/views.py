from django.shortcuts import render # type: ignore
from django.http import HttpResponse  # type: ignore
from .models import Feature

from .forms import FeatureForm
# Create your views here.

def index(request):
    context = {}
    formulario = FeatureForm()
    features = Feature.objects.all()

    context['features'] = features

    if request.method == 'POST':
        if 'guardar' in request.POST:
            identificador = request.POST.get('guardar')
            
            if not identificador:
                formulario = FeatureForm(request.POST)
                
            else:
                feature = Feature.objects.get(id=identificador)
                formulario = FeatureForm(request.POST, instance=feature)
                

            formulario.save()
            formulario = FeatureForm()

        elif 'borrar' in request.POST:
            identificador = request.POST.get('borrar')
            feature = Feature.objects.get(id=identificador)
            feature.delete()

        elif 'editar' in request.POST:
            identificador = request.POST.get('editar')
            feature = Feature.objects.get(id=identificador)

            formulario = FeatureForm(instance=feature)

    context['formulario'] = formulario

    return render(request, 'index.html', context)

def contador(request):

    palabras = request.POST['text'].split()
    cantidadPalabras = len(palabras)
    return render(request, 'contador.html', {"cantidad": cantidadPalabras})