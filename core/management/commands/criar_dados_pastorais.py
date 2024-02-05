# from django.core.management.base import BaseCommand
# from faker import Faker

# from apps.pastorais.models import Pastoral

# fake = Faker(['pt_BR', 'pt-BR'])

# def get_pastorais():
#     nome = fake.company()
#     descricao = fake.paragraph(nb_sentences=3)

#     pastoral_data = dict(
#         nome = nome,
#         descricao = descricao,
#     )

#     return pastoral_data

# def create_pastorais():
#     pastorais_to_create = []
#     for _ in range(5):
#         pastoral_data = get_pastorais()
#         pastorais_to_create.append(Pastoral(**pastoral_data))
#         print(pastoral_data)

#     Pastoral.objects.bulk_create(pastorais_to_create)


# class Command(BaseCommand):
#     help = 'Criar dados fictícios de Pastorais.'

#     def handle(self, *args, **options):
#         create_pastorais()

from django.core.management.base import BaseCommand
from apps.pastorais.models import Pastoral

def create_pastorais():
    pastorais_data = [
        {'nome': 'Pastoral do Dízimo', 'descricao': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat'},
        {'nome': 'Pastoral da Música', 'descricao': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur'},
        {'nome': 'Pastoral da Liturgia', 'descricao': 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo'},
        {'nome': 'Pastoral da Família', 'descricao': 'Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni'},
        {'nome': 'Pastoral da Comunicação', 'descricao': 'But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth'},
    ]

    pastorais_to_create = [Pastoral(**data) for data in pastorais_data]
    print(pastorais_data)

    Pastoral.objects.bulk_create(pastorais_to_create)

class Command(BaseCommand):
    help = 'Criar dados fictícios de Pastorais.'

    def handle(self, *args, **options):
        create_pastorais()