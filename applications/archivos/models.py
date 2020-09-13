from django.db import models

# Create your models here.
from django.db import models
from .managers import carpetaManager
# Create your models here.
class carpeta(models.Model):
    nombre = models.CharField( max_length=50)
    objects=carpetaManager()
    def __str__(self):
        return self.nombre

class modelo(models.Model):
    nombre = models.CharField( max_length=50)
    archivo=models.FileField(upload_to='media/' ,blank=True , null=True)
    carpeta=models.ForeignKey(
        carpeta,
        on_delete=models.CASCADE,
        related_name='carpeta_destino',
      
    )

    def __str__(self):
        return self.nombre