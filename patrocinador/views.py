from django.shortcuts import render
from django.views import generic
from patrocinador.models import Patrocinador
from patrocinador.forms import PatrocinadorForm
from django.urls import reverse_lazy
# Create your views here.

class ListarPatrocinador(generic.ListView):
    model=Patrocinador
    template_name="patrocinador/listar_patrocinador.html"
    context_object_name="obj"
class InsertarPatrocinador(generic.CreateView):
    model=Patrocinador
    template_name="patrocinador/insertar_patrocinador.html"
    context_object_name="obj"
    form_class= PatrocinadorForm
    success_url= reverse_lazy('patrocinador:listar_patrocinador')
class EditarPatrocinador(generic.UpdateView):
    model=Patrocinador
    template_name="patrocinador/insertar_patrocinador.html"
    context_object_name="obj"
    form_class= PatrocinadorForm
    success_url= reverse_lazy('patrocinador:listar_patrocinador')
class EliminarPatrocinador(generic.DeleteView):
    model=Patrocinador
    template_name="patrocinador/eliminar_patrocinador.html"
    context_object_name="obj"
    form_class= PatrocinadorForm
    success_url= reverse_lazy('patrocinador:listar_patrocinador')
