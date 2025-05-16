from django import forms
from .models import RegistroFinanciero

class RegistroForm(forms.ModelForm):
    class Meta:
        model = RegistroFinanciero
        fields = ['tipo', 'monto', 'descripcion']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
