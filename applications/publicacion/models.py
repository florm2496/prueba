from django.db import models

from ckeditor.fields import RichTextField
from django.utils import timezone

class Publicacion(models.Model):
    nombre=models.CharField(max_length=50)
    archivo=models.FileField(upload_to='myfolder/')

    class Meta:
        """Meta definition for Publicacion."""

        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'

    def __str__(self):
       return self.nombre

class Avisos(models.Model):
    detalle=RichTextField()
    fecha=models.DateTimeField(default=timezone.now())

    class Meta:
        verbose_name = 'aviso'
        verbose_name_plural = 'avisos'

    def __str__(self):
       return self.detalle
