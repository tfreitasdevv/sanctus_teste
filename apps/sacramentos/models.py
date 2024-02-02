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


class Eucaristia(models.Model):
    data = models.DateTimeField()
    comungante = models.ForeignKey('pessoas.Paroquiano', related_name='eucaristias_comungante', on_delete=models.CASCADE)
    celebrante = models.ForeignKey('pessoas.Clero', related_name='eucaristias_celebrante', on_delete=models.CASCADE)

    class Meta:
        ordering = ['comungante']

    def __str__(self):
         return f"{self.comungante} - {self.data}"
    

class Crisma(models.Model):
    data = models.DateTimeField()
    crismado = models.ForeignKey('pessoas.Paroquiano', related_name='crismas_crismado', on_delete=models.CASCADE)
    padrinho = models.ForeignKey('pessoas.Paroquiano', related_name='crismas_padrinho', on_delete=models.CASCADE)
    celebrante = models.ForeignKey('pessoas.Clero', related_name='crismas_celebrante', on_delete=models.CASCADE)

    class Meta:
        ordering = ['crismado']

    def __str__(self):
         return f"{self.crismado} - {self.data}"
    

class Matrimonio(models.Model):
    data = models.DateTimeField()
    noivo = models.ForeignKey('pessoas.Paroquiano', related_name='matrimonios_noivo', on_delete=models.CASCADE)
    noiva = models.ForeignKey('pessoas.Paroquiano', related_name='matrimonios_noiva', on_delete=models.CASCADE)
    testemunha1 = models.ForeignKey('pessoas.Paroquiano', related_name='matrimonios_testemunha1', on_delete=models.CASCADE)
    testemunha2 = models.ForeignKey('pessoas.Paroquiano', related_name='matrimonios_testemunha2', on_delete=models.CASCADE)
    celebrante = models.ForeignKey('pessoas.Clero', related_name='matrimonios_celebrante', on_delete=models.CASCADE)

    class Meta:
        ordering = ['noivo']

    def __str__(self):
         return f"{self.noivo} e {self.noiva} - {self.data}"