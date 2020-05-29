from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

class Categoria(models.Model):
    nombre=models.CharField(max_length=30)
    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'  
    def __str__(self):
        return self.nombre
    
    

class Escuela(models.Model):
    nombre=models.CharField(max_length=50)
    class Meta:
        verbose_name='escuela'
        verbose_name_plural='escuelas'
    def __str__(self):
        return self.nombre

class Emergencia(models.Model):
    categoria=models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='categoria_emergencia'
    )
    escuela=models.ForeignKey(
        Escuela,
        on_delete=models.CASCADE,
        related_name='escuela_emergencia'
    )
    descripcion=RichTextField()
    fecha_creacion=models.DateField(default=timezone.now())
    class Meta:
        verbose_name='emergencia'
        verbose_name_plural='emergencias'    
    def __str__(self):
        return str(self.escuela) +'-'+ str( self.categoria)