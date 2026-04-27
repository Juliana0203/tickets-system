from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Ticket(models.Model):  
    ESTADOS = [
        ('abierto', 'Abierto'),
        ('en_espera', 'En espera'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    estado = models.CharField(max_length=20, choices=ESTADOS, default='abierto')
    respuesta_admin = models.TextField(blank=True, null=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
