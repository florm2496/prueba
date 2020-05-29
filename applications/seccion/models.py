from django.db import models

# Create your models here.
from django.db import models
from applications.subdepto.models import Subdepto

class Seccion(models.Model):
    
    subdepto=models.ForeignKey(
        Subdepto,
        on_delete=models.CASCADE,
        related_name='seccion'
    )
    nombre=models.CharField(max_length=30)
    class Meta:
        verbose_name='Seccion'
        verbose_name_plural='Secciones'

    def __str__(self):
        return self.nombre