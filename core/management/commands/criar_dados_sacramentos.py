from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from faker import Faker
import random

from apps.sacramentos.models import Batismo, Crisma, Eucaristia, Matrimonio
from apps.pessoas.models import Clero, Paroquiano

fake = Faker(['pt_BR', 'pt-BR'])

def get_batismos():
    data = fake.date_of_birth(minimum_age=18, maximum_age=65)

    batismos_data = dict(
        data = data,
    )

    return batismos_data

def create_sacramentos():
    batismos_to_create = []
    crismas_to_create = []
    eucaristias_to_create = []
    matrimonios_to_create = []
    paroquiano = Paroquiano.objects.all()
    clero = Clero.objects.all()

    for _ in range(50):
        batismo_data = {
            'data': make_aware(fake.date_time_this_month()),
            'batizado': random.choice(paroquiano),
            'padrinho1': random.choice(paroquiano),
            'padrinho2': random.choice(paroquiano),
            'celebrante': random.choice(clero),
        }

        crisma_data = {
            'data': make_aware(fake.date_time_this_month()),
            'crismado': random.choice(paroquiano),
            'padrinho': random.choice(paroquiano),
            'celebrante': random.choice(clero),
        }

        eucaristia_data = {
            'data': make_aware(fake.date_time_this_month()),
            'comungante': random.choice(paroquiano),
            'celebrante': random.choice(clero),
        }

        matrimonio_data = {
            'data': make_aware(fake.date_time_this_month()),
            'noivo': random.choice(paroquiano),
            'noiva': random.choice(paroquiano),
            'testemunha1': random.choice(paroquiano),
            'testemunha2': random.choice(paroquiano),
            'celebrante': random.choice(clero),
        }

        batismo = Batismo(**batismo_data)
        batismos_to_create.append(batismo)

        crisma = Crisma(**crisma_data)
        crismas_to_create.append(crisma)

        eucaristia = Eucaristia(**eucaristia_data)
        eucaristias_to_create.append(eucaristia)

        matrimonio = Matrimonio(**matrimonio_data)
        matrimonios_to_create.append(matrimonio)

    Batismo.objects.bulk_create(batismos_to_create)
    Crisma.objects.bulk_create(crismas_to_create)
    Eucaristia.objects.bulk_create(eucaristias_to_create)
    Matrimonio.objects.bulk_create(matrimonios_to_create)

class Command(BaseCommand):
    help = 'Criar dados fictícios de Sacramentos'

    def handle(self, *args, **options):
        create_sacramentos()