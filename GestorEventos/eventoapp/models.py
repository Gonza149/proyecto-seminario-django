from django.db import models

# Create your models here.

class Feature(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)
    

