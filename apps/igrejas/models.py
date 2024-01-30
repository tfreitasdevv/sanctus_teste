from django.db import models


class Igreja(models.Model):
    nome = models.CharField(max_length=360, unique=True)

    def __str__(self):
        return self.nome
