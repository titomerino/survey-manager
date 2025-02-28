from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

#models
from survey.models import Assignment, Student
from configuration.models import Menu

#forms
from studentsurvey.forms import UserUpdateForm


def get_user_group(user):
    user_group = user.groups.first()
    menu = Menu.objects.filter(user_group=user_group).first()
    return menu

@login_required(login_url='login')
def home_view(request):
    user = request.user  
    assignments = Assignment.objects.filter(user=user, is_completed=False).prefetch_related('student')

    data = []
    for assignment in assignments:
        student_obj = Student.objects.get(id=assignment.student.id)

        data.append({
            "id": assignment.id,
            "campaign": assignment.campaign,
            "user": assignment.user,
            "student": student_obj
        })

    return render(request, "home.html", {"assignments": data, "menu": get_user_group(user)})


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Formulario no válido.')
    else:
        form = AuthenticationForm()

    # Asignar las clases de bootstrap a los campos del formulario
    form.fields['username'].widget.attrs['class'] = 'form-control'
    form.fields['password'].widget.attrs['class'] = 'form-control'

    return render(request, 'login.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('login') 


@login_required(login_url='login')
def update_profile_view(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Tu perfil ha sido actualizado correctamente.")
    else:
        form = UserUpdateForm(instance=request.user)  # Pre-carga los datos del usuario

    return render(
        request,
        'profile.html',
        {
            'form': form,
            'menu': get_user_group(request.user)
        }
    )