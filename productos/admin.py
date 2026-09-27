from django.contrib import admin
from .models import Producto, ImagenProducto, Contacto , Suscriptor


# ============================================================
# IMÁGENES DEL PRODUCTO
# ============================================================

class ImagenProductoInline(admin.TabularInline):

    model = ImagenProducto

    extra = 4


# ============================================================
# PRODUCTOS
# ============================================================

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):

    inlines = [ImagenProductoInline]


# ============================================================
# CONTACTOS
# ============================================================

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):

    pass

admin.site.register(Suscriptor)