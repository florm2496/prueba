from django.db import models

class PublicacionManager(models.Manager):
  
  def crear_publicacion(self ,archivo,nombre,usuario):
      publicacion=self.model(
        archivo=archivo,
        nombre=nombre,
        usuario=usuario,
      )
      publicacion.save(using=self.db)
      return publicacion

  def publicacion_user(self ,usuario):
        return self.filter(
          usuario_id=usuario
        
        ).order_by('-fecha_creacion')
 