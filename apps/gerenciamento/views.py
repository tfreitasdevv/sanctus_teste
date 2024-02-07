from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'gerenciamento/index.html'


class BaseView(TemplateView):
    template_name = 'gerenciamento/base.html'