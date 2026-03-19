from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = "__all__"
        widgets = {
            'cod_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }