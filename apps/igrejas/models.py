from django.db import models


class Igreja(models.Model):
    nome = models.CharField(max_length=360, unique=True)
    telefone = models.CharField(max_length=30)
    responsavel = models.ForeignKey('pessoas.Clero', related_name='igrejas_responsavel', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
