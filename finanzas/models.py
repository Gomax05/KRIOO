from django.db import models
from django.contrib.auth.models import User

class RegistroFinanciero(models.Model):
    TIPO_CHOICES = [('Ingreso', 'Ingreso'), ('Gasto', 'Gasto'), ('Ahorro', 'Ahorro')]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    monto = models.FloatField()
    descripcion = models.TextField(blank=True)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - {self.monto}"
