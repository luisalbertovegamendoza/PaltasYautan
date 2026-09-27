from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        label="Nombre"
    )

    correo = forms.EmailField(
        label="Correo"
    )

    telefono = forms.CharField(
        max_length=20,
        label="Teléfono"
    )

    mensaje = forms.CharField(
        widget=forms.Textarea,
        label="Mensaje"
    )