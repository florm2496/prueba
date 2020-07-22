from django.shortcuts import render
from django.views.generic import ListView ,DetailView
# Create your views here.
from .models import Departamento
from applications.subdepto.models import Subdepto
from django.contrib.admin.views.decorators import user_passes_test
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.core.paginator import Paginator


class DeptoListView(ListView):
    template_name = 'deptos/deptos.html'
    
    
    def get(self , request , *args , **kwargs):
        
        if request.user.is_superuser:
            deptos=Departamento.objects.all()
            return render(request , 'deptos/deptos.html' ,{'deptos':deptos })
        else:
            return redirect('users_app:user-login')
