from django.contrib import admin
from .models import Funcionario, Clero, Paroquiano
from apps.geral.models import EnderecoFuncionario

class EnderecoFuncionarioInline(admin.StackedInline):
    model = EnderecoFuncionario

class FuncionarioAdmin(admin.ModelAdmin):
    inlines = [EnderecoFuncionarioInline]

admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Clero)
admin.site.register(Paroquiano)
