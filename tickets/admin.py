from django.contrib import admin
from .models import Ticket, Categoria


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'usuario', 'categoria', 'estado', 'fecha_creacion')
    list_filter = ('estado', 'categoria')
    search_fields = ('titulo', 'descripcion')
    readonly_fields = ('usuario', 'fecha_creacion')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
