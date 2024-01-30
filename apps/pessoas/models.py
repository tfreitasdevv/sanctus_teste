from django.db import models


class Pessoa(models.Model):

    OPCOES_GENERO = [
        ('F','Feminino'),
        ('M','Masculino'),
    ]

    nome = models.CharField(max_length=360)
    cpf = models.CharField(max_length=11, unique=True)
    genero = models.CharField(max_length=1, choices=OPCOES_GENERO)
    email = models.EmailField()
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome
