from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
import random

from apps.pessoas.models import Clero
from apps.geral.models import FuncoesClero, EnderecoClero
from apps.igrejas.models import Igreja

fake = Faker(['pt_BR', 'pt-BR'])

def get_cleros():
    nome = fake.name_male()
    cpf = fake.unique.random_number(digits=11)
    genero = fake.random_element(elements=('M', 'M'))
    email = fake.email()
    data_nascimento = fake.date_of_birth(minimum_age=30, maximum_age=75)
    telefone = fake.phone_number()
    cep = fake.postcode()
    logradouro = fake.street_name()
    numero = fake.building_number()
    complemento = fake.street_name()
    bairro = fake.bairro()
    cidade = fake.city()
    estado = fake.state_abbr()
    #funcao = FuncoesClero.objects.get(nome='Padre') # Para definir manualmente a Função
    data_inicio = fake.date_this_decade()
    # igreja = Igreja.objects.get(nome='Alpes') # Para definir manualmente a Igreja

    clero_data = dict(
        nome = nome,
        cpf = cpf,
        genero = genero,
        email = email,
        data_nascimento = data_nascimento,
        telefone = telefone,
        # funcao = funcao, # Usado se Função definida manualmente acima
        data_inicio = data_inicio,
        # igreja = igreja, # Usado se Igreja definida manualmente acima
    )

    endereco_clero_data = dict(
        cep = cep,
        logradouro = logradouro,
        numero = numero,
        complemento = complemento,
        bairro = bairro,
        cidade = cidade,
        estado = estado,
    )

    return clero_data, endereco_clero_data

def create_cleros():
    cleros_to_create = []
    enderecos_clero_to_create = []
    igrejas = Igreja.objects.all()
    funcoes = FuncoesClero.objects.all()

    for _ in range(10):
        clero_data, endereco_clero_data = get_cleros()
        username = fake.user_name()
        password = fake.password()
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()

        igreja = random.choice(igrejas)
        funcao = random.choice(funcoes)

        clero_data['igreja'] = igreja
        clero_data['funcao'] = funcao
        clero_data['usuario'] = user

        clero = Clero(**clero_data)
        endereco_clero_data['clero'] = clero

        cleros_to_create.append(clero)
        enderecos_clero_to_create.append(EnderecoClero(**endereco_clero_data))
    
    print(cleros_to_create)

    Clero.objects.bulk_create(cleros_to_create)
    EnderecoClero.objects.bulk_create(enderecos_clero_to_create)


class Command(BaseCommand):
    help = 'Criar dados fictícios de Clero'

    def handle(self, *args, **options):
        create_cleros()