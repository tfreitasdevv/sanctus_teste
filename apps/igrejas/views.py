from django.views.generic.edit import CreateView, UpdateView
from .models import Igreja


class IgrejaCreate(CreateView):
    model = Igreja
    fields = ['nome']


class IgrejaUpdate(UpdateView):
    model = Igreja
    fields = ['nome']
