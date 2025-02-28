from django.db import models

class Student(models.Model):
    name = models.CharField(
        max_length=50, 
        verbose_name="Nombre"
    )
    last_name = models.CharField(
        max_length=50, 
        verbose_name="Apellidos"
    )
    NIE = models.CharField(
        max_length=15, 
        verbose_name="NIE"
    )
    state = models.BooleanField(
        default=True, 
        verbose_name="Estado"
    )

    def __str__(self):
        return f"{self.name} {self.last_name}"
