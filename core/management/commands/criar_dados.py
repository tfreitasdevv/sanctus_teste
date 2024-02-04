from django.core.management.base import BaseCommand
from faker import Faker

from apps.igrejas.models import Igreja
from core.utils import progressbar

fake = Faker()

def get_igrejas():
    nome = fake.first_name()
    telefone = fake.phone_number()
    data = dict(
        nome = nome,
        telefone = telefone,
    )
    return data

def create_igrejas():
    lista_aux = []
    for _ in range(10):
        data = get_igrejas()
        obj = Igreja(**data)
        print(data)
        lista_aux.append(obj)
    Igreja.objects.bulk_create(lista_aux)


class Command(BaseCommand):
    help = 'Create data.'

    def handle(self, *args, **options):
        create_igrejas()