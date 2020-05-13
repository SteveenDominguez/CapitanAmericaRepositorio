from django.urls import path, include
from companeros.views import ListarCompaneros, InsertarCompaneros, EditarCompaneros, EliminarCompaneros

urlpatterns=[
    path('companeros/list',ListarCompaneros.as_view(),name="listar_companeros"),
    path('companeros/new',InsertarCompaneros.as_view(),name="insertar_companero"),
    path('companeros/edit<int:pk>',EditarCompaneros.as_view(),name="editar_companero"),
    path('companeros/delete<int:pk>',EliminarCompaneros.as_view(),name="eliminar_companero"),
]