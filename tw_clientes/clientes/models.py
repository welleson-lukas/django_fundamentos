from django.db import models

# Create your models here.
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

    def __str__(self):
        return self.nome