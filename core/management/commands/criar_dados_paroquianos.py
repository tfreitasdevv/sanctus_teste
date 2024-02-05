from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
import random

from apps.pessoas.models import Paroquiano
from apps.geral.models import EnderecoParoquiano
from apps.igrejas.models import Igreja

fake = Faker(['pt_BR', 'pt-BR'])

def get_paroquianos():
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
    data_cadastro = fake.date_of_birth(minimum_age=18, maximum_age=65)
    batizado = fake.random_element(elements=(True, False))

    paroquiano_data = dict(
        nome = nome,
        cpf = cpf,
        genero = genero,
        email = email,
        data_nascimento = data_nascimento,
        telefone = telefone,
        data_cadastro = data_cadastro,
        batizado = batizado,
    )

    endereco_paroquiano_data = dict(
        cep = cep,
        logradouro = logradouro,
        numero = numero,
        complemento = complemento,
        bairro = bairro,
        cidade = cidade,
        estado = estado,
    )

    return paroquiano_data, endereco_paroquiano_data

def create_paroquianos():
    paroquianos_to_create = []
    enderecos_paroquianos_to_create = []
    igrejas = Igreja.objects.all()

    for _ in range(20):
        paroquiano_data, endereco_paroquiano_data = get_paroquianos()
        username = fake.user_name()
        password = fake.password()
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()

        igreja = random.choice(igrejas)

        paroquiano_data['igreja'] = igreja
        paroquiano_data['usuario'] = user

        paroquiano = Paroquiano(**paroquiano_data)
        endereco_paroquiano_data['paroquiano'] = paroquiano

        paroquianos_to_create.append(paroquiano)
        enderecos_paroquianos_to_create.append(EnderecoParoquiano(**endereco_paroquiano_data))
    
    print(paroquianos_to_create)

    Paroquiano.objects.bulk_create(paroquianos_to_create)
    EnderecoParoquiano.objects.bulk_create(enderecos_paroquianos_to_create)


class Command(BaseCommand):
    help = 'Criar dados fictícios de Paroquianos'

    def handle(self, *args, **options):
        create_paroquianos()