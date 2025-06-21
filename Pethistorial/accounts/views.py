from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse
from accounts.forms import PerfilForm
from accounts.models import Profile

# Create your views here.

def agregarPerfil(request):
    """
    La función "agregarPerfil" se utiliza para añadir o actualizar la información del perfil de un usuario mediante un formulario.
    
    param request: El objeto request representa la petición HTTP realizada por el usuario. Contiene
    información como la sesión del usuario, el método HTTP utilizado (GET, POST, etc.), y cualquier dato enviado
    con la solicitud
    :return: una plantilla HTML renderizada llamada 'agregarPerfil.html' con los datos del formulario pasados como contexto.
    """
    user = request.user
    profile = Profile.objects.filter(user=user).first()
    form = PerfilForm(instance=profile)
    
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('Perfil')  # O la URL a la que deseas redirigir después de guardar los datos

    return render(request, 'profile/agregarPerfil.html', {'form': form})


