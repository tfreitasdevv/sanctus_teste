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
        nome = nome,
        telefone = telefone,
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
    lista_aux = []
    for _ in range(5):
        igreja_data, enderecoigreja_data = get_igrejas()

        # Criação da Igreja
        igreja = Igreja(**igreja_data)
        igreja.save()

        # Criação do EnderecoIgreja relacionado
        enderecoigreja_data['igreja'] = igreja
        endereco = EnderecoIgreja(**enderecoigreja_data)
        endereco.save()

        print(igreja_data, enderecoigreja_data)
        lista_aux.append(igreja)
    return lista_aux
    # Igreja.objects.bulk_create(lista_aux)


class Command(BaseCommand):
    help = 'Create data.'

    def handle(self, *args, **options):
        create_igrejas()