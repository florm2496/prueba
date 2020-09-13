from django.db import models

class carpetaManager(models.Manager):
    def carpetas(self):
        return self.all()