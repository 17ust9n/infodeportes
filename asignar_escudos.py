import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'infodeportes.settings')
django.setup()

from appdeportes.models import Equipo

base_path = 'media/escudos'

# extensiones posibles
extensiones = ['.png', '.jpg', '.jpeg', '.webp']

for equipo in Equipo.objects.all():
    encontrado = False
    for ext in extensiones:
        nombre_archivo = f"{equipo.nombre}{ext}"
        ruta = os.path.join(base_path, nombre_archivo)

        if os.path.exists(ruta):
            equipo.escudo.name = f"escudos/{nombre_archivo}"
            equipo.save()
            print(f"✅ Escudo asignado a {equipo.nombre}: {nombre_archivo}")
            encontrado = True
            break

    if not encontrado:
        print(f"⚠️ No se encontró imagen para {equipo.nombre}")