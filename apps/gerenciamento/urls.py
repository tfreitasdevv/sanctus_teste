from django.urls import path
from .views import IndexView, BaseView

urlpatterns = [
    path('inicio/', IndexView.as_view(), name='inicio'),
    path('base/', BaseView.as_view(), name='base'),
]
