from django import forms

from apps.profesor.models import Profesor


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ["nombre", "apellido", "dni", "telefono", "email", "fecha_nacimiento"]

        # widgets = {
        #     'nombre': forms.TextInput(attrs={'placeholder': 'Ingresar nombre'}),
        #     'apellido': forms.TextInput(attrs={'placeholder': 'Ingresar apellido'}),
        # }
