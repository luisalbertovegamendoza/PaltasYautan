from django.db import models




class Producto(models.Model):

    nombre = models.CharField(
        max_length=150
    )

    descripcion = models.TextField()

    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    categoria = models.CharField(
        max_length=100,
        blank=True
    )

    precio_oferta = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    stock = models.PositiveIntegerField(
        default=0
    )

    imagen = models.ImageField(
        upload_to='productos/',
        blank=True,
        null=True
    )

    disponible = models.BooleanField(
        default=True
    )

    

    class Meta:

        verbose_name = 'Producto'

        verbose_name_plural = 'Productos'



    def __str__(self):

        return self.nombre
    


class ImagenProducto(models.Model):

    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        related_name='imagenes'
    )

    imagen = models.ImageField(
        upload_to='productos/galeria/'
    )


    def __str__(self):

        return f"Imagen de {self.producto.nombre}"
    



class Contacto(models.Model):
    nombre=models.CharField(max_length=100)
    correo=models.EmailField()
    telefono=models.CharField(max_length=20)
    mensaje=models.TextField()

    fecha=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
class Suscriptor(models.Model):

    correo = models.EmailField(
        unique=True
    )

    fecha_suscripcion = models.DateTimeField(
        auto_now_add=True
    )

    activo = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.correo