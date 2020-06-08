from django.shortcuts import render
from django.views.generic import CreateView ,ListView,DetailView
from .models import Emergencia
from .forms import CrearEmergenciaForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.core.paginator import Paginator
# Create your views here.


class CrearEmergencia(LoginRequiredMixin , CreateView):
    model=Emergencia
    template_name='emergencias/crear_emer.html'
    form_class=CrearEmergenciaForm

    login_url=reverse_lazy('users_app:user-login')

     
    def get_success_url(self):
        return reverse('home_app:index')

class ListarEmergencia(ListView):
    paginate_by=2
    model=Emergencia
    template_name='emergencias/lista_emer.html'
    context_object_name='emergencias'
   
   
    def get(self , request , *args , **kwargs):
        if request.user.is_superuser:
            emergencias=Emergencia.objects.all()
            paginator=Paginator(emergencias ,2)
            page=request.GET.get('page')
            emergencias=paginator.get_page(page)
            return render(request , 'emergencias/lista_emer.html' ,{'emergencias':emergencias})
        else:
            return redirect('users_app:accesodenegado')

    
class EmerDetailView(DetailView):
    model = Emergencia
    template_name = "emergencias/detalle_emer.html"

    