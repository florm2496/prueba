
from django.urls import path 
from .import views
from django.conf import settings
from django.conf.urls.static import static
app_name = "publicacion_app"

def prueba(self):
    print('pruebaaaa')

urlpatterns = [
    path('add_pub/' , views.CrearPublicacion.as_view() , name='add_pub'),
     path('lista_pubs/' , views.ListarPublicacion.as_view() , name='lista_pubs'),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)