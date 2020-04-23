class Pedido():
    def __init__(self, cliente, observacao, valor, data_pedido, status):
        self.__cliente = cliente
        self.__observacao = observacao
        self.__valor = valor
        self.__data_pedido = data_pedido
        self.__status = status

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def observacao(self):
        return self.__observacao

    @observacao.setter
    def observacao(self, observacao):
        self.__observacao = observacao

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def data_pedido(self):
        return self.__data_pedido

    @data_pedido.setter
    def data_pedido(self, data_pedido):
        self.__data_pedido = data_pedido

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status