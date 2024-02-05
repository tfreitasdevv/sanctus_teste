from django.core.management.base import BaseCommand
from faker import Faker

from apps.igrejas.models import Igreja
from apps.geral.models import EnderecoIgreja

fake = Faker(['pt_BR', 'pt-BR'])

def get_igrejas():
    nome = fake.bairro()
    telefone = fake.cellphone_number()
    cep = fake.building_number()
    logradouro = fake.street_name()
    numero = fake.building_number()
    complemento = fake.street_name()
    bairro = fake.bairro()
    cidade = fake.city()
    estado = fake.state_abbr()

    igreja_data = dict(
        nome=nome,
        telefone=telefone,
    )

    enderecoigreja_data = dict(
        cep=cep,
        logradouro=logradouro,
        numero=numero,
        complemento=complemento,
        bairro=bairro,
        cidade=cidade,
        estado=estado,
    )
    
    return igreja_data, enderecoigreja_data

def create_igrejas():
    igrejas_to_create = []
    enderecos_to_create = []

    for _ in range(5):
        igreja_data, enderecoigreja_data = get_igrejas()

        igreja = Igreja(**igreja_data)
        enderecoigreja_data['igreja'] = igreja

        igrejas_to_create.append(igreja)
        enderecos_to_create.append(EnderecoIgreja(**enderecoigreja_data))

    print(igrejas_to_create, enderecos_to_create)
    
    Igreja.objects.bulk_create(igrejas_to_create)
    EnderecoIgreja.objects.bulk_create(enderecos_to_create)

class Command(BaseCommand):
    help = 'Criar dados fictícios de Igrejas com seus endereços.'

    def handle(self, *args, **options):
        create_igrejas()