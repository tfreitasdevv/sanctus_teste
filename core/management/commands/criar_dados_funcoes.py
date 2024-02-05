from django.core.management.base import BaseCommand
from apps.geral.models import FuncoesClero, FuncoesFuncionarios

# def create_funcoes_clero():
#     funcoes_clero_data = [
#         {'nome': 'Pároco'},
#         {'nome': 'Padre'},
#         {'nome': 'Diácono'},
#     ]

#     funcoes_clero_to_create = [FuncoesClero(**data) for data in funcoes_clero_data]
#     print(funcoes_clero_data)

#     FuncoesClero.objects.bulk_create(funcoes_clero_to_create)

# def create_funcoes_funcionarios():
#     funcoes_funcionarios_data = [
#         {'nome': 'Secretário'},
#         {'nome': 'Auxiliar de Serviços Gerais'},
#         {'nome': 'Zelador'},
#     ]

#     funcoes_funcionarios_to_create = [FuncoesFuncionarios(**data) for data in funcoes_funcionarios_data]
#     print(funcoes_funcionarios_data)

#     FuncoesFuncionarios.objects.bulk_create(funcoes_funcionarios_to_create)

def create_funcoes():
    funcoes_clero_data = [
        {'nome': 'Pároco'},
        {'nome': 'Padre'},
        {'nome': 'Diácono'},
    ]

    funcoes_funcionarios_data = [
        {'nome': 'Secretário'},
        {'nome': 'Auxiliar de Serviços Gerais'},
        {'nome': 'Zelador'},
    ]

    funcoes_clero_to_create = [FuncoesClero(**data) for data in funcoes_clero_data]
    print(funcoes_clero_data)
    funcoes_funcionarios_to_create = [FuncoesFuncionarios(**data) for data in funcoes_funcionarios_data]
    print(funcoes_funcionarios_data)

    FuncoesClero.objects.bulk_create(funcoes_clero_to_create)
    FuncoesFuncionarios.objects.bulk_create(funcoes_funcionarios_to_create)


class Command(BaseCommand):
    help = 'Criar dados fictícios das Funções do Clero e Funcionários.'

    def handle(self, *args, **options):
        create_funcoes()