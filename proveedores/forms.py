from django import forms
from .models import Proveedores

class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedores
        fields = "__all__"
        widgets = {
            'nro_proveedor': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cuit': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }