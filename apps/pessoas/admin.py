from django.contrib import admin
from .models import Funcionario, Clero, Paroquiano
from apps.geral.models import EnderecoFuncionario, EnderecoClero, EnderecoParoquiano

# Inserção inline do endereço do Funcionário

class EnderecoFuncionarioInline(admin.StackedInline):
    model = EnderecoFuncionario


class FuncionarioAdmin(admin.ModelAdmin):
    inlines = [EnderecoFuncionarioInline]

# Inserção inline do endereço do Clero


class EnderecoCleroInline(admin.StackedInline):
    model = EnderecoClero


class CleroAdmin(admin.ModelAdmin):
    inlines = [EnderecoCleroInline]

# Inserção inline do endereço do Paroquiano

class EnderecoParoquianoInline(admin.StackedInline):
    model = EnderecoParoquiano


class ParoquianoAdmin(admin.ModelAdmin):
    inlines = [EnderecoParoquianoInline]

admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Clero, CleroAdmin)
admin.site.register(Paroquiano, ParoquianoAdmin)
