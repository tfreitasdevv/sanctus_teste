from django.contrib import admin
from .models import Funcionario, Clero, Paroquiano

admin.site.register(Funcionario)
admin.site.register(Clero)
admin.site.register(Paroquiano)
