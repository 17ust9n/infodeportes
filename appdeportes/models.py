from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    deporte = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    fundado_en = models.IntegerField()

    def __str__(self):
        return self.nombre
