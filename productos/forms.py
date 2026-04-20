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


class ProductoUpdateForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ["cod_producto", "descripcion", "precio", "cantidad"]
        widgets = {
            "cod_producto": forms.NumberInput(attrs={'class': 'form-control'}),
            "descripcion": forms.TextInput(attrs={'class': 'form-control'}),
            "precio": forms.TextInput(attrs={'class': 'form-control'}),
            "cantidad": forms.NumberInput(attrs={'class': 'form-control'}),
        }