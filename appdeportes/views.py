from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Equipo
from .forms import RegistroForm

# --- VISTAS EXISTENTES ---
def inicio(request):
    return render(request, 'inicio.html')

def acerca(request):
    return render(request, 'acerca.html')

@login_required
def lista_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'equipos.html', {'equipos': equipos})

@login_required
def detalle_equipo(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    return render(request, 'equipo_detalle.html', {'equipo': equipo})

@login_required
def amistoso(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    return render(request, 'amistoso.html', {'equipo': equipo})

# --- VISTAS DE USUARIO ---
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login_view')
