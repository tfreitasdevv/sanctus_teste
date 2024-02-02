from django.contrib import admin
from .models import Igreja
from apps.geral.models import EnderecoIgreja

# Inserção inline do endereço da Igreja

class EnderecoIgrejaInline(admin.StackedInline):
    model = EnderecoIgreja


class IgrejaAdmin(admin.ModelAdmin):
    inlines = [EnderecoIgrejaInline]

admin.site.register(Igreja, IgrejaAdmin)
