import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'infodeportes.settings')
django.setup()

from appdeportes.models import Equipo

base_path = 'media/estadios'
extensiones = ['.png', '.jpg', '.jpeg', '.webp']

for equipo in Equipo.objects.all():
    encontrado = False
    for ext in extensiones:
        # Normalizamos el nombre (sin espacios y minúsculas)
        nombre_archivo = f"{equipo.nombre.lower().replace(' ', '_')}{ext}"
        ruta = os.path.join(base_path, nombre_archivo)

        if os.path.exists(ruta):
            equipo.estadio.name = f"estadios/{nombre_archivo}"  # 👈 usar el nombre correcto del campo
            equipo.save()
            print(f"✅ Foto de estadio asignada a {equipo.nombre}: {nombre_archivo}")
            encontrado = True
            break

    if not encontrado:
        print(f"⚠️ No se encontró imagen para el estadio de {equipo.nombre}")
