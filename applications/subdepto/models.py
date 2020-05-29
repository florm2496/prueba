from django.db import models
from applications.prueba1.models import Departamento

class Subdepto(models.Model):
    
    depto=models.ForeignKey(
        Departamento,
        on_delete=models.CASCADE,
        related_name='subdepto'
    )
    nombre=models.CharField(max_length=30)
    class Meta:
        verbose_name='Division'
        verbose_name_plural='Divisiones'

    def __str__(self):
        return self.nombre + str(self.id)