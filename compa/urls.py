from django.urls import path, include
from compa.views import ListarCompas, InsertarCompa, EditarCompa, EliminarCompa

urlpatterns=[
    path('compa/list',ListarCompas.as_view(),name="listar_compas"),
    path('compa/new',InsertarCompa.as_view(),name="insertar_compa"),
    path('compa/edit<int:pk>',EditarCompa.as_view(),name="editar_compa"),
    path('compa/delete<int:pk>',EliminarCompa.as_view(),name="eliminar_compa"),
]