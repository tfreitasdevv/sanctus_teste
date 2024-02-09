from django.urls import path
from .views import IgrejaCreate, IgrejaUpdate

urlpatterns = [
    path('novo', IgrejaCreate.as_view(), name='igreja_create'),
    path('editar/<int:pk>', IgrejaUpdate.as_view(), name='igreja_update'),
]