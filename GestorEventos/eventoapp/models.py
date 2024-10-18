from django.db import models

# Create your models here.

class Feature(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre    

class Lugar(models.Model):
    nombre  = models.CharField(max_length=50)
    calle = models.CharField(max_length=50)
    numero = models.IntegerField()
    detalleLugar = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nombre

class TipoEvento(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fechaEvento = models.DateField()
    ubicacion = models.ForeignKey(Lugar, null=True, on_delete=models.CASCADE)
    tipoEvento = models.ForeignKey(TipoEvento, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + '-' + self.ubicacion.nombre