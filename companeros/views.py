from django.shortcuts import render
from django.views import generic
from companeros.models import Companeros
from companeros.forms import CompanerosForm
from django.urls import reverse_lazy
# Create your views here.

class ListarCompaneros(generic.ListView):
    model=Companeros
    template_name="companeros/listar_companeros.html"
    context_object_name="obj"
class InsertarCompaneros(generic.CreateView):
    model=Companeros
    template_name="companeros/insertar_companeros.html"
    context_object_name="obj"
    form_class= CompanerosForm
    success_url= reverse_lazy('companeros:listar_companeros')
class EditarCompaneros(generic.UpdateView):
    model=Companeros
    template_name="companeros/insertar_companeros.html"
    context_object_name="obj"
    form_class= CompanerosForm
    success_url= reverse_lazy('companeros:listar_companeros')
class EliminarCompaneros(generic.DeleteView):
    model=Companeros
    template_name="companeros/eliminar_companeros.html"
    context_object_name="obj"
    form_class= CompanerosForm
    success_url= reverse_lazy('companeros:listar_companeros')
