from django.shortcuts import render
from django.http import JsonResponse 
from .serializers import FeatureSerializer, TipoEventoSerializer, LugarSerializer, EventoSerializer
from .models import Feature, TipoEvento, Lugar, Evento
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def index(request):

    return render(request, 'index.html')


@api_view(["GET", "POST"])
def listaFeatures(request, format=None):
    
    if request.method == "GET":
        features = Feature.objects.all()
        serializer = FeatureSerializer(features, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = FeatureSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)

@api_view(["GET","PUT","DELETE"])
def detalleFeature(request, id, format=None):
    
    try:
        feature = Feature.objects.get(pk=id)                                              
    except Feature.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = FeatureSerializer(feature)
        return Response(serializer.data)
    
    if request.method == "PUT":
        serializer = FeatureSerializer(feature, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        feature.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(["GET","POST"])
def listaTipoEventos(request, format=None):

    if request.method == "GET":
        tipoeventos = TipoEvento.objects.all()
        serializer = TipoEventoSerializer(tipoeventos, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = TipoEventoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
@api_view(["GET", "POST"])
def listaLugares(request, format=None):

    if request.method == "GET":
        lugares = Lugar.objects.all()
        serializer = LugarSerializer(lugares, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = LugarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)

@api_view(["GET","POST"])
def listaEventos(request, format=None):

    if request.method == "GET":
        eventos = Evento.objects.all()
        serializer = EventoSerializer(eventos, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = EventoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED) 