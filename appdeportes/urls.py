from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login_view'),  # ahora login es la principal
    path('inicio/', views.inicio, name='inicio'),
    path('acerca/', views.acerca, name='acerca'),
    path('equipos/', views.lista_equipos, name='lista_equipos'),
    path('equipo/<int:pk>/', views.detalle_equipo, name='detalle_equipo'),

    # --- nuevas rutas para usuarios ---
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.logout_view, name='logout'),
]
