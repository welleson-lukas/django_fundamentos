from ..models import Pedido

def cadatrar_pedido(pedido):
    Pedido.objects.create(cliente=pedido.cliente, data_pedido=pedido.data_pedido, valor=pedido.valor,
                          status=pedido.status, observacao=pedido.observacao)

def listar_pedidos():
    pedidos = Pedido.objects.all()
    return pedidos