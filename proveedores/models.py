from django.db import models

class Proveedores(models.Model):

    nro_proveedor = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    cuit = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre