from django.db import models


class Batismo(models.Model):
    data = models.DateTimeField()
    batizado = models.ForeignKey('pessoas.Paroquiano', related_name='batismos_batizado', on_delete=models.CASCADE)
    padrinho1 = models.ForeignKey('pessoas.Paroquiano', related_name='batismos_padrinho1', on_delete=models.CASCADE)
    padrinho2 = models.ForeignKey('pessoas.Paroquiano', related_name='batismos_padrinho2', on_delete=models.CASCADE)
    celebrante = models.ForeignKey('pessoas.Clero', related_name='batismos_celebrante', on_delete=models.CASCADE)

    class Meta:
        ordering = ['batizado']

    def __str__(self):
         return f"{self.batizado} - {self.data}"
    
