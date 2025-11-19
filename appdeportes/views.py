from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Equipo, PartidoAmistoso
from .forms import RegistroForm
import random

# --- VISTAS GENERALES ---
def inicio(request):
    return render(request, 'inicio.html')

def acerca(request):
    return render(request, 'acerca.html')


# --- VISTAS DE EQUIPOS ---
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


# --- VISTA PARTIDO AMISTOSO ---
@login_required
def amistoso(request):
    equipos = Equipo.objects.all()
    resultado = None
    goles_vos = goles_pc = None
    equipo_vos = equipo_pc = None

    if request.method == "POST":
        equipo_vos_id = request.POST.get("equipo_vos")

        if not equipo_vos_id:
            return render(request, "amistoso.html", {
                "equipos": equipos,
                "error": "Debes elegir un equipo antes de jugar."
            })

        equipo_vos = Equipo.objects.get(id=int(equipo_vos_id))

        # PC elige un equipo distinto al tuyo
        equipo_pc = random.choice(Equipo.objects.exclude(id=equipo_vos.id))

        # Goles
        goles_vos = int(request.POST.get("goles_vos", 0))
        goles_pc = random.randint(0, 5)

        # Resultado
        if goles_vos > goles_pc:
            resultado = "¡Ganaste! 🎉"
        elif goles_vos < goles_pc:
            resultado = "¡Gana la PC! 🤖"
        else:
            resultado = "¡EMPATE! ⚖️"

        PartidoAmistoso.objects.create(
            usuario=request.user,        # ← ✔ NECESARIO
            equipo_vos=equipo_vos,
            equipo_pc=equipo_pc,
            goles_vos=goles_vos,
            goles_pc=goles_pc,
            resultado=resultado
        )


    # Historial completo (o solo del usuario si tu modelo tiene usuario)
    historial = PartidoAmistoso.objects.filter(usuario=request.user).order_by('-id')

    return render(request, "amistoso.html", {
        "equipos": equipos,
        "resultado": resultado,
        "goles_vos": goles_vos,
        "goles_pc": goles_pc,
        "equipo_vos": equipo_vos,
        "equipo_pc": equipo_pc,
        "historial": historial
    })


# --- VISTA LISTA DE PARTIDOS (todos los usuarios) ---
@login_required
def lista_partidos(request):
    partidos = PartidoAmistoso.objects.all().order_by('-id')
    return render(request, 'lista_partidos.html', {'partidos': partidos})


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
