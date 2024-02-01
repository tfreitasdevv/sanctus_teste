from django.db import models


class Igreja(models.Model):
    nome = models.CharField(max_length=360, unique=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
