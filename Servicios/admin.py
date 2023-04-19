from django.contrib import admin
from .models import Servicio

# Register your models here.

#Define que los campos "created" y "updated" del modelo "Servicio" son de solo lectura
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

#Permite a los usuarios con permisos adecuados acceder y administrar los objetos a través de la interfaz de administración de Django
admin.site.register(Servicio, ServicioAdmin)