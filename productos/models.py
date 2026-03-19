from django.db import models

class Productos(models.Model):

    cod_producto = models.IntegerField(unique=True)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.descripcion
