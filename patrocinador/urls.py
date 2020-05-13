from django.urls import path, include
from patrocinador.views import ListarPatrocinador, InsertarPatrocinador, EditarPatrocinador, EliminarPatrocinador

urlpatterns=[
    path('patrocinador/list',ListarPatrocinador.as_view(),name="listar_patrocinador"),
    path('patrocinador/new',InsertarPatrocinador.as_view(),name="insertar_patrocinador"),
    path('patrocinador/edit<int:pk>',EditarPatrocinador.as_view(),name="editar_patrocinador"),
    path('patrocinador/delete<int:pk>',EliminarPatrocinador.as_view(),name="eliminar_patrocinador"),
]