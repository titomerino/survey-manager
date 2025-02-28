from django.db import models

class Teacher(models.Model):
    name = models.CharField(
        max_length=50, 
        verbose_name="Nombre"
    )
    last_name = models.CharField(
        max_length=50, 
        verbose_name="Apellidos"
    )
    email = models.EmailField(
        max_length=100, 
        verbose_name="Correo"
    )
    phone = models.CharField(
        max_length=15, 
        verbose_name="Teléfono"
    )
    state = models.BooleanField(
        default=True, 
        verbose_name="Estado"
    )

    def __str__(self):
        return f"{self.name} {self.last_name}"
