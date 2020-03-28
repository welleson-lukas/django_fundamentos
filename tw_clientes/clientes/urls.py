from django.urls import path
from .views import *

urlpatterns = [
    path('listar', listar_clientes, name='listar_clientes'),
    path('cadastrar', inserir_cliente, name='cadastrar_cliente'),
    path('listar/<int:id>', listar_clientes_id, name='listar_clientes_id'),
    path('editar/<int:id>', editar_cliente, name='editar_cliente'),
    path('remover/<int:id>', remover_cliente, name='remover_cliente')
]