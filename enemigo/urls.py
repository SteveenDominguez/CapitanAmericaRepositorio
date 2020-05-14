from django.urls import path, include
from enemigo.views import ListarEnemigos, InsertarEnemigo, EditarEnemigo, EliminarEnemigo

urlpatterns=[
    path('enemigo/list',ListarEnemigos.as_view(),name="listar_enemigos"),
    path('enemigo/new',InsertarEnemigo.as_view(),name="insertar_enemigo"),
    path('enemigo/edit<int:pk>',EditarEnemigo.as_view(),name="editar_enemigo"),
    path('enemigo/delete<int:pk>',EliminarEnemigo.as_view(),name="eliminar_enemigo"),
]