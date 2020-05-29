from django.shortcuts import render
from .models import Publicacion
from django.urls import reverse_lazy, reverse
from .forms import PublicacionForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import (
    CreateView
)


class CrearPublicacion(LoginRequiredMixin,CreateView):
     template_name="publicacion/add_pub.html"
     model =Publicacion
     form_class =PublicacionForm
     login_url=reverse_lazy('users_app:user-login')

     
     def get_success_url(self):
        return reverse('index')
