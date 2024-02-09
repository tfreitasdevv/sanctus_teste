from django.urls import path
from .views import IgrejaCreate

urlpatterns = [
    path('novo', IgrejaCreate.as_view(), name='igreja_create'),
]