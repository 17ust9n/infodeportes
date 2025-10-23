from django.db import models

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

    def __str__(self):
        return self.nombre
