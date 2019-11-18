from django.db import models
from apps.marca.models import Marca
from apps.categoriaProducto.models import CategoriaProducto

# Create your models here.
class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    #existencias = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    ESTADO = (
        ('A', 'ACTIVO'),
        ('D', 'DESHABILITADO')
    )
    estado = models.CharField(max_length=1, choices=ESTADO, default='A')