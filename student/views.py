from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

#models
from .models import Student
#funcions
from studentsurvey.commons import ModuleContextMixin
# Forms
from .forms import StudentForm


class StudentListView(LoginRequiredMixin, UserPassesTestMixin, ModuleContextMixin, ListView):
    model = Student
    template_name = "student/student_list.html"
    context_object_name = "data"
    paginate_by = 8
    login_url = reverse_lazy("login")

    def test_func(self):
        """Verifica si el usuario pertenece al grupo 'admin'."""
        return self.request.user.groups.filter(name="admin").exists()

class StudentCreateView(UserPassesTestMixin, LoginRequiredMixin, ModuleContextMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = "student/student_form.html"
    success_url = reverse_lazy("student_list")
    login_url = reverse_lazy("login")

    def test_func(self):
        """Verifica si el usuario pertenece al grupo 'admin'."""
        return self.request.user.groups.filter(name="admin").exists()


class StudentUpdateView(UserPassesTestMixin, LoginRequiredMixin, ModuleContextMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "student/student_form.html"
    login_url = reverse_lazy("login")

    def test_func(self):
        """Verifica si el usuario pertenece al grupo 'admin'."""
        return self.request.user.groups.filter(name="admin").exists()
    
    def form_valid(self, form):
        """Después de guardar, redirige a la misma página de edición."""
        self.object = form.save()
        messages.success(self.request, "Los cambios se han guardado correctamente.")
        return redirect(self.request.path)


@login_required(login_url='login')
def student_delete_view(request, pk):

    if not request.user.groups.filter(name="admin").exists():
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('home')
    
    student = get_object_or_404(Student, pk=pk)
    student_name = f"{student.name} {student.last_name}"
    student.delete()
    messages.success(request, f'Estudiante {student_name} ha sido eliminado.')
    
    return redirect('student_list')