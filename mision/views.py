from django.shortcuts import render
from django.views import generic
from mision.models import Mision
from mision.forms import MisionForm
from django.urls import reverse_lazy
# Create your views here.

class ListarMision(generic.ListView):
    model=Mision
    template_name="mision/listar_mision.html"
    context_object_name="obj"
class InsertarMision(generic.CreateView):
    model=Mision
    template_name="mision/insertar_mision.html"
    context_object_name="obj"
    form_class= MisionForm
    success_url= reverse_lazy('mision:listar_mision')
class EditarMision(generic.UpdateView):
    model=Mision
    template_name="mision/insertar_mision.html"
    context_object_name="obj"
    form_class= MisionForm
    success_url= reverse_lazy('mision:listar_mision')
class EliminarMision(generic.DeleteView):
    model=Mision
    template_name="mision/eliminar_mision.html"
    context_object_name="obj"
    form_class= MisionForm
    success_url= reverse_lazy('mision:listar_mision')
