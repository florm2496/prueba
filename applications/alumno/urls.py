#
from django.urls import path

from . import views

app_name = "alumno_app"

urlpatterns = [
    path('add/' , views.AddAlumno.as_view() , name='Add'),

]