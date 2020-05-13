from django.urls import include, path
from aliado.views import ListarAliados, InsertarAliados, EditarAliado, EliminarAliado

urlpatterns = [
    path('aliado/list',ListarAliados.as_view(),name='listar_aliados'),
    path('aliado/new',InsertarAliados.as_view(),name='insertar_aliado'),
    path('aliado/edit<int:pk>',EditarAliado.as_view(),name='editar_aliado'),
    path('aliado/delete<int:pk>',EliminarAliado.as_view(),name='eliminar_aliado'),
]