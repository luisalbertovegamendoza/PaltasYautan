from django.shortcuts import render , redirect
from django.views.generic import ListView , TemplateView
from django.contrib import messages

from .models import Producto , Contacto , Suscriptor
from .forms import ContactoForm



class IndexView(TemplateView):
    template_name='productos/nosotros.html'


class ListaProductosView(ListView):
    model=Producto
    template_name='productos/lista.html'
    context_object_name = 'productos'


def contacto(request):

    enviado = False

    if request.method == 'POST':

        form = ContactoForm(request.POST)

        if form.is_valid():

            Contacto.objects.create(
                nombre=form.cleaned_data['nombre'],
                correo=form.cleaned_data['correo'],
                telefono=form.cleaned_data['telefono'],
                mensaje=form.cleaned_data['mensaje']
            )

            enviado = True
            form = ContactoForm()

    else:
        form = ContactoForm()

    return render(
        request,
        'contacto.html',
        {
            'form': form,
            'enviado': enviado
        }
    )

# ============================
# SUSCRIPCIÓN
# ============================

def suscribirse(request):

    if request.method == 'POST':

        correo = request.POST.get('correo', '').strip().lower()

        if correo:

            suscriptor, creado = Suscriptor.objects.get_or_create(
                correo=correo
            )

            if creado:

                messages.success(
                    request,
                    '¡Gracias por suscribirte! Recibirás nuestras promociones y novedades.'
                )

            else:

                messages.info(
                    request,
                    'Este correo ya está suscrito a nuestras promociones.'
                )

    return redirect(
        request.META.get('HTTP_REFERER', '/')
    )