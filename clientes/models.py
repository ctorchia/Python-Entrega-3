from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_de_nacimiento = models.DateField(
        blank="",
        null=True,
        default=None
    )
    nro_cliente = models.IntegerField(unique=True)
    dni = models.CharField(max_length=12, unique=True)
    email = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return f"Cliente({self.nro_cliente}): {self.nombre} {self.apellido} - {self.dni}"
