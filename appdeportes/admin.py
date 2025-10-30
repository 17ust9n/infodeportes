from django.contrib import admin
from .models import Equipo

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de objetos
    list_display = ('nombre', 'anio_fundacion', 'apodo', 'cantidad_hinchas', 'cantidad_copas', 'clasico_rival')
    
    # Campos que podés buscar
    search_fields = ('nombre', 'apodo', 'clasico_rival')
    
    # Filtros laterales por campos
    list_filter = ('anio_fundacion',)
