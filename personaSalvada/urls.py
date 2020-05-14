from django.urls import path, include
from personaSalvada.views import ListarPersonasSalvadas, InsertarPersonaSalvada, EditarPersonaSalvada, EliminarPersonaSalvada

urlpatterns=[
    path('personaSalvada/list',ListarPersonasSalvadas.as_view(),name="listar_personasSalvadas"),
    path('personaSalvada/new',InsertarPersonaSalvada.as_view(),name="insertar_personaSalvada"),
    path('personaSalvada/edit<int:pk>',EditarPersonaSalvada.as_view(),name="editar_personaSalvada"),
    path('personaSalvada/delete<int:pk>',EliminarPersonaSalvada.as_view(),name="eliminar_personaSalvada"),
]