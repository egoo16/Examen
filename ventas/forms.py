from django import forms
from .models import Usuario, Producto, Compra

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ('usuario', 'producto', 'cantidad')

def __init__ (self, *args, **kwargs):
        super(PeliculaForm, self).__init__(*args, **kwargs)
        self.fields["usuario"].widget = forms.CheckboxSelectMultiple()
        self.fields["usuario"].help_text = "Ingrese los usuarios"
        self.fields["usuario"].queryset = Usuario.objects.all()

        self.fields["producto"].widget = forms.CheckboxSelectMultiple()
        self.fields["producto"].help_text = "Ingrese los Productos que se compran"
        self.fields["producto"].queryset = Producto.objects.all()
