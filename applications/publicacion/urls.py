
from django.urls import path 
from .import views


app_name = "publicacion_app"

def prueba(self):
    print('pruebaaaa')

urlpatterns = [
    path('add_pub/' , views.CrearPublicacion.as_view() , name='add_pub'),
]