from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.gerenciamento.urls')),
    path('igrejas/', include('apps.igrejas.urls')),
]
