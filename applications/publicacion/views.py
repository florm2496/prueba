from django.shortcuts import render
from .models import Publicacion
from django.urls import reverse_lazy, reverse
from .forms import PublicacionForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import (
    CreateView, DetailView ,TemplateView,ListView,View
)
from django.core.paginator import Paginator
from django.http import FileResponse, Http404

class CrearPublicacion(LoginRequiredMixin,CreateView):
     template_name="publicacion/add_pub.html"
     model =Publicacion
     form_class =PublicacionForm
     login_url=reverse_lazy('users_app:user-login')

     def form_valid(self, form):
    
        publicacion=form.save(commit=False)
        publicacion.usuario=self.request.user
        publicacion.save()
        
        return HttpResponseRedirect(
                reverse(
                'publicacion_app:lista_pubs'
            )
        )


class ListarPublicacion(ListView):
    model=Publicacion
    template_name='publicacion/lista_pubs.html'
    context_object_name='publicaciones'



def pub_list(request):
    publicacion=Publicacion.objects.all()
    return render(request , 'publicacion/ver.html' ,{'publicacion':publicacion})
  
