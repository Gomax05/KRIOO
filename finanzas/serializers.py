from rest_framework import serializers
from .models import RegistroFinanciero

class RegistroFinancieroSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroFinanciero
        fields = ['id', 'usuario', 'tipo', 'monto', 'descripcion', 'fecha']
        read_only_fields = ['usuario', 'fecha']
