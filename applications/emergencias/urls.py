#
from django.urls import path
from .views import CrearEmergencia ,ListarEmergencia
from . import views

app_name = "emergencias_app"

urlpatterns = [ 
   path('crear_emer/', CrearEmergencia.as_view() , name='crear_emer'),
   path('lista_emer/', ListarEmergencia.as_view() , name='lista_emer'),
   ]