from django.views.generic.edit import CreateView
from .models import Igreja


class IgrejaCreate(CreateView):
    model = Igreja
    fields = ['nome']
