from django.contrib import admin
from django.urls import path, include  # include es para incluir URLs de la app
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),       # Ruta para el admin de Django
    path('', include('appdeportes.urls')), # Todas las demás URLs las maneja la app

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)