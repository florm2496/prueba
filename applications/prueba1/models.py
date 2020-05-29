from django.db import models


class Departamento(models.Model):

    nombre=models.CharField('nombre' , max_length=50)
    activo=models.BooleanField('activo' ,default=True)

    class Meta:


        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamento'

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.nombre + str(self.id)
