from rest_framework import serializers
from .models import Feature, TipoEvento, Lugar

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'nombre', 'descripcion']

class TipoEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEvento
        fields = ['id', 'nombre']

class LugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugar
        fields = ['id', 'nombre']