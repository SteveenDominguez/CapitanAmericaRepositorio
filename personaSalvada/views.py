from django.shortcuts import render
from personaSalvada.models import PersonaSalvada
from django.views import generic
from personaSalvada.forms import PersonaSalvadaForm
from django.urls import reverse_lazy
from django.http import HttpResponse
# Create your views here.
class ListarPersonasSalvadas(generic.ListView):
    model=PersonaSalvada
    template_name="personaSalvada/listar_personasSalvadas.html"
    context_object_name="cosa"

class InsertarPersonaSalvada(generic.CreateView):
    model=PersonaSalvada
    template_name="personaSalvada/insertar_personaSalvada.html"
    context_object_name="obj"
    form_class=PersonaSalvadaForm
    success_url=reverse_lazy("personaSalvada:listar_personasSalvadas")

class EditarPersonaSalvada(generic.UpdateView):
    model=PersonaSalvada
    template_name="personaSalvada/insertar_personaSalvada.html"
    context_object_name="obj"
    form_class=PersonaSalvadaForm
    success_url=reverse_lazy("personaSalvada:listar_personasSalvadas")

class EliminarPersonaSalvada(generic.DeleteView):
    model=PersonaSalvada
    template_name="personaSalvada/eliminar_personaSalvada.html"
    context_object_name="obj"
    form_class=PersonaSalvadaForm
    success_url=reverse_lazy("personaSalvada:listar_personasSalvadas")