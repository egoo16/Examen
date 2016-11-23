from django import forms
from .models import Usuario, Producto, Compra

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ('usuarios', 'productos', 'cantidad')

def __init__ (self, *args, **kwargs):
        super(PeliculaForm, self).__init__(*args, **kwargs)
        self.fields["usuarios"].widget = forms.CheckboxSelectMultiple()
        self.fields["usuarios"].help_text = "Ingrese los usuarios"
        self.fields["usuarios"].queryset = Usuario.objects.all()

        self.fields["productos"].widget = forms.CheckboxSelectMultiple()
        self.fields["productos"].help_text = "Ingrese los Productos que se compran"
        self.fields["productos"].queryset = Producto.objects.all()
