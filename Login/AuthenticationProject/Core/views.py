from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from .models import *
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

@login_required
def Home(request):
    return render(request, 'index.html')

def RegisterView(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_data_has_error = False

        if User.objects.filter(username=username).exists():
            user_data_has_error = True
            messages.error(request, "El nombre de usuario ya existe")

        if User.objects.filter(email=email).exists():
            user_data_has_error = True
            messages.error(request, "El email ya esta registrado")

        if len(password) < 8:
            user_data_has_error = True
            messages.error(request, "La contraseña debe contener almenos 8 caracteres")

        if user_data_has_error:
            return redirect('register')
        else:
            new_user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )
            messages.success(request, "Cuenta creada exitosamente")
            return redirect('login')


    return render(request, 'register.html')

def LoginView(request):

    if request.method == 'POST':

        #getting user input from frontend
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # login user if login credentials are correct
            login(request, user)

            return redirect('home')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
            return redirect('login')

    return render(request, 'login.html')

def LogoutView(request):

    logout(request)

    #redirect to logi n page after logout
    return redirect('login')


def ForgotPassword(request):

    if request.method == "POST":
        email = request.POST.get('email')

        try:
            user = User.objects.get(email=email)

            new_password_reset = PasswordReset(user=user)
            new_password_reset.save()

            password_reset_url = reverse('reset-password', kwargs={'reset_id': new_password_reset.reset_id})

            full_password_reset_url = f'{request.scheme}://{request.get_host()}{password_reset_url}'

            email_body = f'Resetea tu contraseña usando el siguiente link:\n\n\n{full_password_reset_url}'
        
            email_message = EmailMessage(
                'Resetea tu contraseña', # email subject
                email_body,
                settings.EMAIL_HOST_USER, # email sender
                [email] # email  receiver 
            )

            email_message.fail_silently = True
            email_message.send()

            return redirect('password-reset-sent', reset_id=new_password_reset.reset_id)

        except User.DoesNotExist:
            messages.error(request, f"El email: '{email}' no se encuentra registrado")
            return redirect('forgot-password')

    return render(request, 'forgot_password.html')


def PasswordResetSent(request, reset_id):

    if PasswordReset.objects.filter(reset_id=reset_id).exists():
        return render(request, 'password_reset_sent.html')
    else:
        #redirect to forgot password page if code does not exist
        messages.error(request, 'Id de reseteo invalida')
        return redirect('forgot-password')

def ResetPassword(request, reset_id):
    try:
        password_reset_id = PasswordReset.objects.get(reset_id=reset_id)

        if request.method == "POST":
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            passwords_have_error = False

            if not password or not confirm_password:
                passwords_have_error = True
                messages.error(request, 'Rellena todos los apartados')

            if password != confirm_password:
                passwords_have_error = True
                messages.error(request, 'Las contraseñas no coinciden')

            if len(password) < 5:
                passwords_have_error = True
                messages.error(request, 'La contraseña debe tener almenos 5 caracteres')

            expiration_time = password_reset_id.created_when + timezone.timedelta(minutes=10)

            if timezone.now() > expiration_time:
                passwords_have_error = True
                messages.error(request, 'El link ha expirado')

                password_reset_id.delete()

            if not passwords_have_error:
                user = password_reset_id.user
                user.set_password(password)
                user.save()

                password_reset_id.delete()

                messages.success(request, 'Contraseña reseteada. Inicia seción')
                return redirect('login')
            else:
                return render(request, 'reset_password.html', {'reset_id': reset_id})

    except PasswordReset.DoesNotExist:
        messages.error(request, 'ID de reseteo invalido')
        return redirect('forgot-password')

    return render(request, 'reset_password.html')

class ListaPendientes(LoginRequiredMixin, ListView):
    model = Tarea
    context_object_name = 'tareas'

    def get_context_data(self, **kwarg):
        context = super().get_context_data(**kwarg)
        context['tareas'] = context['tareas'].filter(usuario=self.request.user)
        context['count'] = context['tareas'].filter(completo=False).count()

        valor_buscado = self.request.GET.get('area-buscar') or ''
        if valor_buscado:
            context['tareas'] = context['tareas'].filter(titulo__icontains=valor_buscado)
        context['valor_buscado'] = valor_buscado
        return context

class DetalleTarea(LoginRequiredMixin, DetailView):
    model = Tarea
    context_object_name = 'tarea'
    template_name = 'tarea.html'

class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'completo']
    success_url = reverse_lazy('tareas')

class EditarTarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'completo']
    success_url = reverse_lazy('tareas')

class EliminarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    context_object_name = 'tarea'
    success_url = reverse_lazy('tareas')