from django.db import models


class FuncoesFuncionarios(models.Model):
    nome = nome = models.CharField(max_length=360)

    def __str__(self):
        return self.nome
