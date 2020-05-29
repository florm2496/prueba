from django.shortcuts import render
from django.forms import formset_factory
# Create your views here.
from django.views.generic.edit import FormView
from .forms import AlumnoForm, AsistenciaForm

class AddAlumno(FormView):
    template_name='alumno/add.html'
    form_class=formset_factory(AlumnoForm , extra=1)
    success_url='.'

    def form_valid(self , form):
        for f in form:
            print(f.cleaned_data['nombre'])
            f.save()

        return super(AddAlumno ,self).form_valid(form)