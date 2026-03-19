from django import forms
from .models import Productos

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Productos
        fields = "__all__"
        widgets = {
            'cod_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }