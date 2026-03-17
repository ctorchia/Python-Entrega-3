from django import forms
from .models import Clientes

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ["nombre", "apellido", "fecha_de_nacimiento", "dni", "email", "nro_cliente"]
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "nro_cliente": forms.NumberInput(attrs={'class': 'form-control'}),
            "apellido": forms.TextInput(attrs={'class': 'form-control'}),
            "fecha_de_nacimiento": forms.DateInput(attrs={'class': 'form-control'}),
            "dni": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'})
        }