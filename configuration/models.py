from django.db import models
from django.contrib.auth.models import Group

class Menu(models.Model):
    title = models.CharField(max_length=255, verbose_name="Título")
    user_group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Grupo de usuarios")  # Moved to Menu

    class Meta:
        verbose_name = "Menú"
        verbose_name_plural = "Menús"

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    text_link = models.CharField(max_length=255, verbose_name="Texto del enlace")
    url = models.CharField(verbose_name="URL", max_length=250)
    icon = models.CharField(max_length=100, verbose_name="Ícono")  # Ejemplo: "bi bi-house"
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="menu_items", verbose_name="Menú")

    class Meta:
        verbose_name = "Ítem de Menú"
        verbose_name_plural = "Ítems de Menú"

    def __str__(self):
        return f"{self.text_link} ({self.menu.title})"
