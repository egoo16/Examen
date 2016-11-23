from django.db import models
from django.contrib import admin
from django.utils import timezone

# Create your models here.

class Producto(models.Model):
    codigo  =   models.CharField(max_length=7)
    nombre  =   models.CharField(max_length=30)
    foto = models.ImageField(upload_to='imagen/')
    Lala = 'LA'
    Selada = 'SE'
    Real = 'RE'
    Cola = 'CL'
    MARCAS_C = (
            (Lala, 'Lala'),
            (Selada, 'Selada'),
            (Real, 'Real'),
            (Cola, 'Cola'),
        )
    marca = models.CharField(
            max_length=2,
            choices=MARCAS_C,
            default=Lala,
        )
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    existencia = models.IntegerField()
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    dpi = models.CharField(max_length=15)
    nombre = models.CharField(max_length=60)
    productos = models.ManyToManyField(Producto, through='Compra')

    def __str__(self):
        return self.nombre

class Compra (models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(default=timezone.now)

class CompraInLine(admin.TabularInline):
    model = Compra
    extra = 1

class ProductoAdmin(admin.ModelAdmin):
    inlines = (CompraInLine,)

class UsuarioAdmin (admin.ModelAdmin):
    inlines = (CompraInLine,)
