from django.contrib import admin
from django.urls import path
from . import views 

app_name='prueba_app'

urlpatterns = [
    path('uploadfile/' ,views.uploadfile , name='uploadurl'),
    path('home/' ,views.home , name='home'),
    path('listaarchivos/' ,views.ArchivosListView.as_view() , name='listaarchivos'),
    path('crearcarpetas/' ,views.crearCarpeta , name='crearcarpetas'),
    path('listarcarpetas/' ,views.listarCarpeta.as_view() , name='listarcarpetas')
 
]
