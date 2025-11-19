from django.db import models
from django.contrib.auth.models import User

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)

    cantidad_hinchas = models.CharField(
        max_length=100,
        help_text="Cantidad de hinchas aproximadamente (puede no ser exacta)",
        blank=True,
        null=True
    )
    
    cantidad_copas = models.CharField(
        max_length=100,
        help_text="Cantidad de copas, títulos, veces que ganó el torneo, etc",
        blank=True,
        null=True
    )

    clasico_rival = models.CharField(
        max_length=100,
        help_text="Clásico rival y cuántos partidos le lleva",
        blank=True,
        null=True
    )


    apodo = models.CharField(
        max_length=100,
        help_text="Apodo del club, los hinchas y su estadio",
        blank=True,
        null=True
    )
    anio_fundacion = models.PositiveIntegerField(
        help_text="Año de fundación del club",
        blank=True,
        null=True
    )
    escudo = models.ImageField(
        upload_to='escudos/',
        blank=True,
        null=True,
        help_text="Foto del escudo del club"
    )

    nombre_estadio = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Nombre del estadio del club"
    )

    estadio = models.ImageField(
        upload_to='estadios/',
        blank=True,
        null=True,
        help_text="Foto del estadio del club"
    )

    ubicacion_estadio = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Ubicación del estadio (dirección)"
    )

    mapa = models.TextField(
        blank=True,
        null=True,
        help_text="Código embed del mapa de Google Maps (iframe)"
    )

    def __str__(self):
        return self.nombre


class PartidoAmistoso(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # <-- Agregado
    equipo_vos = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='equipo_vos')
    equipo_pc = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='equipo_pc')
    goles_vos = models.IntegerField()
    goles_pc = models.IntegerField()
    resultado = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.equipo_vos} {self.goles_vos} - {self.goles_pc} {self.equipo_pc}"
