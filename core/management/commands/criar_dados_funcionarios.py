from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
import random
from datetime import date, timedelta

from apps.pessoas.models import Funcionario
from apps.geral.models import FuncoesFuncionarios, EnderecoFuncionario
from apps.igrejas.models import Igreja

fake = Faker(['pt_BR', 'pt-BR'])

def get_funcionarios():
    nome = fake.first_name()
    cpf = fake.unique.random_number(digits=11)
    genero = fake.random_element(elements=('F', 'M'))
    email = fake.email()
    data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=65)
    telefone = fake.phone_number()
    cep = fake.building_number()
    logradouro = fake.street_name()
    numero = fake.building_number()
    complemento = fake.street_name()
    bairro = fake.bairro()
    cidade = fake.city()
    estado = fake.state_abbr()
    #funcao = FuncoesFuncionarios.objects.get(nome='Zelador') # Para definir manualmente a Igreja
    data_admissao = fake.date_of_birth(minimum_age=18, maximum_age=65)
    # igreja = Igreja.objects.get(nome='Alpes') # Para definir manualmente a Igreja

    funcionario_data = dict(
        nome = nome,
        cpf = cpf,
        genero = genero,
        email = email,
        data_nascimento = data_nascimento,
        telefone = telefone,
        # funcao = funcao, # Usado se Função definida manualmente acima
        data_admissao = data_admissao,
        # igreja = igreja, # Usado se Igreja definida manualmente acima
    )

    endereco_funcionario_data = dict(
        cep = cep,
        logradouro = logradouro,
        numero = numero,
        complemento = complemento,
        bairro = bairro,
        cidade = cidade,
        estado = estado,
    )

    return funcionario_data, endereco_funcionario_data

def create_funcionarios():
    funcionarios_to_create = []
    enderecos_funcionario_to_create = []
    igrejas = Igreja.objects.all()
    funcoes = FuncoesFuncionarios.objects.all()

    for _ in range(5):
        funcionario_data, endereco_funcionario_data = get_funcionarios()
        username = fake.user_name()
        password = fake.password()
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()

        igreja = random.choice(igrejas)
        funcao = random.choice(funcoes)

        funcionario_data['igreja'] = igreja
        funcionario_data['funcao'] = funcao
        funcionario_data['usuario'] = user

        funcionario = Funcionario(**funcionario_data)
        endereco_funcionario_data['funcionario'] = funcionario

        funcionarios_to_create.append(funcionario)
        enderecos_funcionario_to_create.append(EnderecoFuncionario(**endereco_funcionario_data))
    
    print(funcionarios_to_create)

    Funcionario.objects.bulk_create(funcionarios_to_create)
    EnderecoFuncionario.objects.bulk_create(enderecos_funcionario_to_create)


class Command(BaseCommand):
    help = 'Criar dados fictícios de Funcionários'

    def handle(self, *args, **options):
        create_funcionarios()