from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListaProductosView.as_view() , name='lista_productos'),
    path('nosotros/', views.IndexView.as_view() , name='nosotros'),

    path(
        'contacto/',
        views.contacto,
        name='contacto'
    ),
  
    path(
        'suscribirse/',
        views.suscribirse,
        name='suscribirse'
    ),
  
]