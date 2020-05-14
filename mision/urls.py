from django.urls import path, include
from mision.views import ListarMision, InsertarMision, EditarMision, EliminarMision

urlpatterns=[
    path('mision/list',ListarMision.as_view(),name="listar_mision"),
    path('mision/new',InsertarMision.as_view(),name="insertar_mision"),
    path('mision/edit<int:pk>',EditarMision.as_view(),name="editar_mision"),
    path('mision/delete<int:pk>',EliminarMision.as_view(),name="eliminar_mision"),
]