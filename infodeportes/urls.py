from django.contrib import admin
from django.urls import path, include  # include es para incluir URLs de la app

urlpatterns = [
    path('admin/', admin.site.urls),       # Ruta para el admin de Django
    path('', include('appdeportes.urls')), # Todas las demás URLs las maneja la app
]
