from django.shortcuts import render
from django.views import generic
from compa.models import Compa
from django.urls import reverse_lazy
from compa.forms import CompaForm
from django.urls import reverse_lazy
# Create your views here.

class ListarCompas(generic.ListView):
    model=Compa
    template_name="compa/listar_compas.html"
    context_object_name="obj"

class InsertarCompa(generic.CreateView):
    model=Compa
    template_name="compa/insertar_compa.html"
    context_object_name="obj"
    form_class= CompaForm
    success_url= reverse_lazy('compa:listar_compas')
class EditarCompa(generic.UpdateView):
    model=Compa
    template_name="compa/insertar_compa.html"
    context_object_name="obj"
    form_class= CompaForm
    success_url= reverse_lazy('compa:listar_compas')
class EliminarCompa(generic.DeleteView):
    model=Compa
    template_name="compa/eliminar_compa.html"
    context_object_name="obj"
    form_class= CompaForm
    success_url= reverse_lazy('compa:listar_compas')
