from django.contrib import admin
from .models import FuncoesFuncionarios, FuncoesClero, EnderecoParoquiano, EnderecoClero, EnderecoFuncionario, EnderecoIgreja

admin.site.register(FuncoesFuncionarios)
admin.site.register(FuncoesClero)
admin.site.register(EnderecoParoquiano)
admin.site.register(EnderecoClero)
admin.site.register(EnderecoFuncionario)
admin.site.register(EnderecoIgreja)
