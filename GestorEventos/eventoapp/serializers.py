from rest_framework import serializers
from .models import Feature, TipoEvento, Lugar, Evento

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

class EventoSerializer(serializers.ModelSerializer):
    ubicacion = serializers.PrimaryKeyRelatedField(queryset=Lugar.objects.all())

    class Meta:
        model = Evento
        fields = ['id', 'nombre', 'fechaEvento', 'ubicacion', 'tipoEvento']

    def to_representation(self, instance):
        
        representation = super().to_representation(instance)
        ubicacion = instance.ubicacion
        representation['ubicacion'] = LugarSerializer(ubicacion).data
        return representation