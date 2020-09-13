from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy ,reverse
# Create your views here.
from django.views.generic import CreateView,TemplateView ,ListView
from django.views.generic.edit import FormView
from .models import modelo , carpeta
from .forms import uploadForm , carpetaForm
from django.http import HttpResponseRedirect

from .managers import carpetaManager




def home(request):
    return render(request , 'home.html' ,{})



def uploadfile(request):
    
    if request.method == 'POST':
        form= uploadForm(request.POST , request.FILES)
        car=request.POST['carpeta']
        i_c=carpeta.objects.get(id=car)   #creando una instancia de carpeta
        print(type(i_c))
   
        files=request.FILES.getlist('archivo')
        if form.is_valid():
            for f in files:
                instancia=modelo(archivo=f)
                nombre=instancia.archivo
                instancia.nombre=nombre
                instancia.carpeta=i_c
                instancia.save()
                form=uploadForm()
        return HttpResponseRedirect(reverse_lazy('prueba_app:listaarchivos'))  
    else:
        form=uploadForm()
    return render(request ,'archivos/uploadfile.html' , {'form':form})

class ArchivosListView(ListView):
    model = modelo
    template_name = "archivos/listaarchivos.html"
    context_object_name='archivos'
    def get_queryset(self):
        carpeta=self.request.GET.get('kword','')
        if carpeta!='':
            lista=modelo.objects.filter(
            carpeta__nombre=carpeta
        )
            return lista
        else:
            lista=modelo.objects.all()
            return lista

class listarCarpeta(TemplateView):
    template_name='archivos/carpetas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lista'] = carpeta.objects.carpetas()
        #formulario de creacion de carpeta
        context['form']=carpetaForm
        #se puede enviar cualquier objeto de python como comntexto
        return context


def crearCarpeta(request):
    if request.method=='POST':
        form=carpetaForm(request.POST)
        if form.is_valid:
            form.save()
        return HttpResponseRedirect(reverse('prueba_app:listarcarpetas'))
        
    else:
        form=carpetaForm
    return render(request, 'archivos/carpetas.html' ,{'form':form})
