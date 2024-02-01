from django.db import models


class Pastoral(models.Model):
    nome = models.CharField(max_length=360)
    descricao = models.TextField()

    class Meta:
        ordering = ['nome']
        verbose_name_plural = 'Pastorais'

    def __str__(self):
        return self.nome
