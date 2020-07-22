from django.contrib import admin
from django.urls import path 
from .views import DeptoListView #,SubdeptoListView

from django.contrib.admin.views.decorators import user_passes_test
app_name = "depto_app"

def prueba(self):
    print('pruebaaaa')

urlpatterns = [
    path('prueba/' ,prueba),
    path('deptos/' ,DeptoListView.as_view() ,name='deptos'),
     #path('divisiones/' ,SubdeptoListView.as_view() ,name='subdeptos'),
]