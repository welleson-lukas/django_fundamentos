from django.db import models
from django.utils import timezone

# Create your models here.
class Endereco(models.Model):
    numero = models.IntegerField(null=False, blank=False)
    complemento = models.CharField(max_length=200, null=False, blank=False)
    rua = models.CharField(max_length=200, null=False, blank=False)
    bairro = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.CharField(max_length=50, null=False, blank=False)
    pais = models.CharField(max_length=50, null=False, blank=False)


    def __str__(self):
        return self.rua

class Pedido(models.Model):
    STATUS_CHOICE = (
        ("R", "Realizado"),
        ("A", "Andamento"),
        ("E", "Entrega"),
    )
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(default=timezone.now)
    valor = models.FloatField(blank=False, null=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, blank=False, null=False)
    observacao = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.cliente.nome

class Cliente(models.Model):

    SEXO_CHOICE = (

        ("F","Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )

    nome = models.CharField(max_length=100, null=False, blank=False) # 'CharField'EQUIVALENTE AO VARCHAR DO MYSQL
    data_nascimento = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    profissao = models.CharField(max_length=50, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICE, blank=False, null=False)

    # RELACIONAMENTO 1 PARA 1 COM A CLASSE ENDEREÇO
    endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

