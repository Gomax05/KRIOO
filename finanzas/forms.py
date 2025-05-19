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
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
