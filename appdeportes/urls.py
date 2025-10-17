from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('acerca/', views.acerca, name='acerca'),
    path('equipos/', views.lista_equipos, name='lista_equipos'),
    path('equipo/<int:pk>/', views.detalle_equipo, name='detalle_equipo'),
]
