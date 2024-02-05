from django.core.management.base import BaseCommand
from faker import Faker

from apps.pastorais.models import Pastoral

fake = Faker(['pt_BR', 'pt-BR'])

def get_pastorais():
    nome = fake.company()
    descricao = fake.paragraph(nb_sentences=3)

    pastoral_data = dict(
        nome = nome,
        descricao = descricao,
    )

    return pastoral_data

def create_pastorais():
    lista_aux = []
    for _ in range(5):
        pastoral_data = get_pastorais()

        # Criação da Igreja
        pastoral = Pastoral(**pastoral_data)
        pastoral.save()

        print(pastoral_data)
        lista_aux.append(pastoral)
    return lista_aux
    # Igreja.objects.bulk_create(lista_aux)


class Command(BaseCommand):
    help = 'Criar dados fictícios de Pastorais.'

    def handle(self, *args, **options):
        create_pastorais()