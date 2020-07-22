from django.db import models

from ckeditor.fields import RichTextField
from model_utils.models import TimeStampedModel
from .managers import PublicacionManager
from django.conf import settings

class Publicacion(TimeStampedModel):
    nombre=models.CharField(max_length=50)

    archivo=models.FileField(upload_to='myfolder/')

    usuario=models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name='usuario'
    )
    objects=PublicacionManager()
    class Meta:
        """Meta definition for Publicacion."""

        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'

    def __str__(self):
       return self.nombre
    


