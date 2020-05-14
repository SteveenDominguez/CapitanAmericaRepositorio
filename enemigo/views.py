from django.shortcuts import render
from enemigo.models import Enemigo
from django.views import generic
from enemigo.forms import EnemigoForm
from django.urls import reverse_lazy
from django.http import HttpResponse
# Create your views here.
class ListarEnemigos(generic.ListView):
    model=Enemigo
    template_name="enemigo/listar_enemigos.html"
    context_object_name="cosa"

class InsertarEnemigo(generic.CreateView):
    model=Enemigo
    template_name="enemigo/insertar_enemigo.html"
    context_object_name="obj"
    form_class=EnemigoForm
    success_url=reverse_lazy("enemigo:listar_enemigos")

class EditarEnemigo(generic.UpdateView):
    model=Enemigo
    template_name="enemigo/insertar_enemigo.html"
    context_object_name="obj"
    form_class=EnemigoForm
    success_url=reverse_lazy("enemigo:listar_enemigos")

class EliminarEnemigo(generic.DeleteView):
    model=Enemigo
    template_name="enemigo/eliminar_enemigo.html"
    context_object_name="obj"
    form_class=EnemigoForm
    success_url=reverse_lazy("enemigo:listar_enemigos")