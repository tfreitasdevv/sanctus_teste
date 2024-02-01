from django.db import models
from django.contrib.auth.models import User
from apps.geral.models import FuncoesFuncionarios, FuncoesClero
from apps.igrejas.models import Igreja


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
    telefone = models.CharField(max_length=30)

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    igreja = models.ForeignKey(Igreja, on_delete=models.CASCADE)

    class Meta:
        abstract = True
        ordering = ['nome']


class Funcionario(Pessoa):
    funcao = models.ForeignKey(FuncoesFuncionarios,on_delete=models.CASCADE)
    data_admissao = models.DateField()
    data_demissao = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['nome']
        verbose_name_plural = 'Funcionarios'

    def __str__(self):
        return f"{self.nome} - {self.funcao}"
    

class Clero(Pessoa):
    funcao = models.ForeignKey(FuncoesClero,on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_saida = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['nome']
        verbose_name_plural = 'Clero'

    def __str__(self):
        return f"{self.nome} - {self.funcao}"
    

class Paroquiano(Pessoa):
    batizado = models.BooleanField(default=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nome']
        verbose_name_plural = 'Paroquianos'

    def __str__(self):
        return self.nome
