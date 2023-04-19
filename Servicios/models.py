from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='servicios')
    created = models.DateTimeField(auto_now_add=True) #fecha de creación
    updated = models.DateTimeField(auto_now_add=True) #fecha de actualización

    #establecer metadatos en el modelo de Djang
    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"

    # Devuelve el título del servicio
    def __str__(self):
        return self.titulo