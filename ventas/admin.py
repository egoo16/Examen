from django.contrib import admin
from ventas.models import Producto, ProductoAdmin, Usuario, UsuarioAdmin, Compra

#Registramos nuestras clases principales.
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Compra)
