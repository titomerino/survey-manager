from configuration.models import Menu
from django.contrib import messages
from django.shortcuts import redirect


def get_user_group(user):
    user_group = user.groups.first()
    menu = Menu.objects.filter(user_group=user_group).first()
    return menu


class ModuleContextMixin:
    def handle_no_permission(self):
        """Muestra un mensaje de error y redirige a 'home' si el usuario no tiene permisos."""
        messages.error(self.request, "No tienes permiso para acceder a esta página.")
        return redirect("home")

    def get_context_data(self, **kwargs):
        """Añade datos adicionales al contexto."""
        context = super().get_context_data(**kwargs)
        context["menu"] = get_user_group(self.request.user)
        return context
