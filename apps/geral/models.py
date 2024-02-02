from django.db import models


class FuncoesFuncionarios(models.Model):
    nome = models.CharField(max_length=360)

    class Meta:
        ordering = ['nome']
        verbose_name_plural = 'Funções Funcionários'

    def __str__(self):
        return self.nome


class FuncoesClero(models.Model):
    nome = models.CharField(max_length=360)

    class Meta:
        ordering = ['nome']
        verbose_name_plural = 'Funções Clero'

    def __str__(self):
        return self.nome


class EnderecoFuncionario(models.Model):
    funcionario = models.OneToOneField('pessoas.Funcionario', on_delete=models.CASCADE)
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=200)
    numero = models.CharField(max_length=15)
    complemento = models.CharField(max_length=100)
    bairro = models.CharField(max_length=360)
    cidade = models.CharField(max_length=360)
    estado = models.CharField(max_length=360)


class EnderecoClero(models.Model):
    funcionario = models.OneToOneField('pessoas.Clero', on_delete=models.CASCADE)
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=200)
    numero = models.CharField(max_length=15)
    complemento = models.CharField(max_length=100)
    bairro = models.CharField(max_length=360)
    cidade = models.CharField(max_length=360)
    estado = models.CharField(max_length=360)


class EnderecoParoquiano(models.Model):
    funcionario = models.OneToOneField('pessoas.Paroquiano', on_delete=models.CASCADE)
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=200)
    numero = models.CharField(max_length=15)
    complemento = models.CharField(max_length=100)
    bairro = models.CharField(max_length=360)
    cidade = models.CharField(max_length=360)
    estado = models.CharField(max_length=360)


class EnderecoIgreja(models.Model):
    igreja = models.OneToOneField('igrejas.Igreja', on_delete=models.CASCADE)
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=200)
    numero = models.CharField(max_length=15)
    complemento = models.CharField(max_length=100)
    bairro = models.CharField(max_length=360)
    cidade = models.CharField(max_length=360)
    estado = models.CharField(max_length=360)