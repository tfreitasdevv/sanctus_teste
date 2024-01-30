from django.db import models
from django.contrib.auth.models import User


class Pessoa(models.Model):

    OPCOES_GENERO = [
        ('F','Feminino'),
        ('M','Masculino'),
    ]

    nome = models.CharField(max_length=360)
    #usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cpf = models.CharField(max_length=11, unique=True)
    genero = models.CharField(max_length=1, choices=OPCOES_GENERO)
    email = models.EmailField()
    data_nascimento = models.DateField()

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        abstract=True

class Funcionario(Pessoa):
    funcao = models.CharField(max_length=360)
    data_admissao = models.DateField()
    data_demissao = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome
    