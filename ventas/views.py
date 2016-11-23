from django.shortcuts import render
# Create your views here.
from django.contrib import messages
from .forms import CompraForm
from ventas.models import Producto, Compra, Usuario

#Vista para insertar una nueva película y los actores que actúan en ella.
def CompraNueva(request):
    if request.method == "POST":
        formulario = CompraForm(request.POST)
        if formulario.is_valid():
            for usuario_id in request.POST.getlist('usuario'):
                for producto_id in request.POST.getlist('producto'):
                    compra = Compra(usuario_id=usuario_id, producto_id = producto_id,cantidad = formulario.cleaned_data['cantidad'])
                    compra.save()
                    messages.add_message(request, messages.SUCCESS, 'Compra Realizada Exitosamente')
    else:
        formulario = CompraForm()
    return render(request, 'ventas/compra_nueva.html', {'formulario': formulario})
