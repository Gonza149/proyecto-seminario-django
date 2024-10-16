from django.contrib import admin

from .models import Feature, Lugar, Evento, TipoEvento
# Register your models here.

admin.site.register(Feature)
admin.site.register(Lugar)
admin.site.register(Evento)
admin.site.register(TipoEvento)