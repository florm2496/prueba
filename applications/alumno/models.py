from django.db import models
from django.utils import timezone
# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    legajo = models.IntegerField()

    class Meta:
        """Meta definition for Alumno."""

        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'

    def __str__(self):
        return self.nombre

class Asistencia(models.Model):
    alumno=models.ForeignKey(
        Alumno,
        on_delete=models.CASCADE
    )
    fecha=models.DateField(default=timezone.now)
    
    class Meta:
        verbose_name='asistencia'
        verbose_name_plural='asistencias'

    def __str__(self):
        return self.nombre