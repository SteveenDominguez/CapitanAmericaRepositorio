from django.shortcuts import render
from aliado.models import Aliado
from django.views import generic
from aliado.forms import AliadoForm
from django.urls import reverse_lazy
from django.http import HttpResponse
# Create your views here.
class ListarAliados(generic.ListView):
    model=Aliado
    template_name="aliado/listar_aliados.html"
    context_object_name="cosa"

class InsertarAliados(generic.CreateView):
    model=Aliado
    template_name="aliado/insertar_aliado.html"
    context_object_name="obj"
    form_class=AliadoForm
    success_url=reverse_lazy("aliado:listar_aliados")

class EditarAliado(generic.UpdateView):
    model=Aliado
    template_name="aliado/insertar_aliado.html"
    context_object_name="obj"
    form_class=AliadoForm
    success_url=reverse_lazy("aliado:listar_aliados")

class EliminarAliado(generic.DeleteView):
    model=Aliado
    template_name="aliado/eliminar_aliado.html"
    context_object_name="obj"
    form_class=AliadoForm
    success_url=reverse_lazy("aliado:listar_aliados")