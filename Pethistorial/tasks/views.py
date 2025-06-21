from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse
from accounts.forms import PerfilForm,MascotaForm1,VacunacionForm,DesparacitacionForm,AtencionForm
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login




def home(request):
    """
    La función `home` devuelve una plantilla HTML renderizada para la página de inicio.
    
    parámetro request: El parámetro request es un objeto que representa la petición HTTP realizada por el
    usuario. Contiene información sobre la petición, como el método utilizado (GET o POST), las cabeceras
    el agente de usuario y los datos enviados con la solicitud. En este caso, el objeto de solicitud se pasa a
    el renderizado
    :return: la plantilla renderizada 'tareas/home.html'.
    """
    return render(request,'tasks/home.html')

@login_required
def Perfil(request):
    """
    La función "Perfil" es una función de vista en Django que gestiona la creación y visualización de perfiles de usuario.
    de usuario.
    
    :param request: El parámetro `request` es un objeto que representa la petición HTTP realizada por el
    usuario. Contiene información sobre la petición, como el usuario que la realiza, el método
    utilizado (GET o POST), y cualquier dato enviado con la petición.
    :return: una plantilla HTML renderizada llamada 'profile/Perfil.html' junto con un diccionario de contexto
    que contiene las variables 'form' y 'user'.
    """
    user = request.user  # Obtener el usuario actualmente autenticado

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        form1 = PerfilForm(request.POST)
        if form.is_valid() and form1.is_valid():
            # Guardar los datos del formulario en la base de datos
            form.save()

            # Redireccionar al detalle del perfil
            return redirect('perfil')
    else:
        form = CustomUserCreationForm(initial={
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        })
        

    return render(request, 'profile/Perfil.html', {'form': form, 'user': user})



def exit(request):
    """
    La función `exit` cierra la sesión del usuario y lo redirige a la página de inicio.
    
    param petición: El parámetro `request` es un objeto que representa la petición HTTP realizada por el
    usuario. Contiene información sobre la petición, como la URL, las cabeceras y cualquier dato enviado con la petición.
    con la solicitud. En este caso, se utiliza para cerrar la sesión del usuario y redirigirlo a la página de inicio
    :return: una redirección a la página 'home'.
    """
    logout(request)
    return redirect('home')

def register(request):
    """
    La función `register` maneja el registro de usuarios validando los datos del formulario, creando un nuevo usuario,
    autenticando al usuario, y redirigiendo a la página de inicio.
    
    param request: El parámetro `request` es un objeto que representa la petición HTTP realizada por el
    usuario. Contiene información sobre la petición, como el método utilizado (GET o POST), la sesión del usuario y cualquier dato enviado con la petición.
    y cualquier dato enviado con la petición
    :return: El código devuelve una plantilla HTML llamada 'registration/register.html' con el diccionario de datos
    diccionario de datos como contexto.
    """
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            
            return redirect('home')
    return render(request,'registration/register.html', data)

def nosotros(request):
    """
    La función "nosotros" renderiza la plantilla "nosotros.html".
    
    param petición: El parámetro `request` es un objeto que representa la petición HTTP realizada por el
    cliente. Contiene información sobre la petición, como el método HTTP utilizado (GET, POST, etc.),
    las cabeceras, el agente de usuario y el cuerpo de la petición. En este caso, el objeto `request` es
    :return: la plantilla renderizada 'tareas/nosotros.html'
    """
    return render(request,'tasks/nosotros.html')







@login_required  
def agregarMascota(request):
    """
    La función "agregarMascota" es una función de vista en Django que añade una nueva mascota a la base de datos,
    asociada al usuario conectado en ese momento.
    
    :param request: El objeto request representa la petición HTTP que el usuario realizó para acceder a la
    vista. Contiene información como la sesión del usuario, el método HTTP utilizado (GET o POST), y
    cualquier dato enviado en la solicitud
    :return: una plantilla HTML renderizada llamada 'mascotas/agregarMascota.html' con una variable de contexto
    que contiene el formulario.
    """
    form = MascotaForm1()
    if request.method == 'POST':
        form = MascotaForm1(request.POST)
        if form.is_valid():
            mascota = form.save(commit=False)
            mascota.rut_user = request.user.profile  # Asignar el rut_user al perfil del usuario actual
            mascota.save()
            return redirect('NMascotas')
    
    context = {'form': form}
    return render(request, 'mascotas/agregarMascota.html', context)





def NMascotas(request):
    # Obtener el usuario actualmente autenticado
    user = request.user

    # Filtrar las mascotas en base al usuario actual
    mascotas_list = Mascota.objects.filter(rut_user_id=user.id)

    context = {
        'mascotas': mascotas_list
    }
    return render(request, 'mascotas/NMascotas.html', context)

from accounts.models import Mascota, Vacunacion,Desparacitacion,Atencion






def infomascotas(request, mascota_id):
    """
    La función `infomascotas` recupera información sobre una mascota concreta, incluyendo sus vacunas
    desparasitaciones y atenciones médicas, y la muestra en una plantilla.
    
    parámetro request: El parámetro request es un objeto que representa la petición HTTP realizada por el
    cliente. Contiene información como el método de solicitud, las cabeceras y el cuerpo.
    :param mascota_id: El parámetro `mascota_id` es el ID de la mascota de la que se desea obtener información.
    recuperar información. Se utiliza para obtener el objeto mascota específico de la base de datos mediante la función
    consulta `Mascota.objects.get(id=mascota_id)`.
    :return: una plantilla HTML renderizada llamada `infomascotas.html` con los datos del contexto.
    """
    mascota = Mascota.objects.get(id=mascota_id)
    vacunaciones = Vacunacion.objects.filter(mascota=mascota)
    desparasitaciones = Desparacitacion.objects.filter(mascota=mascota)
    atenciones = Atencion.objects.filter(mascota=mascota)

    context = {
        'mascota': mascota,
        'vacunaciones': vacunaciones,
        'desparasitaciones': desparasitaciones,
        'atenciones': atenciones,
    }

    return render(request, 'mascotas/infomascotas.html', context)



def agregar_vacunacion(request, mascota_id):
    """
    La función "agregar_vacunacion" agrega un registro de vacunación para una mascota específica.
    
    :param request: El objeto request representa la petición HTTP que ha realizado el usuario para acceder a la
    vista. Contiene información como la sesión del usuario, el método HTTP utilizado (GET, POST, etc.)
    y cualquier dato enviado con la solicitud
    :param mascota_id: El parámetro `mascota_id` es el ID de la mascota para la que queremos
    añadir un registro de vacunación
    :return: una plantilla HTML renderizada llamada `mascotas/agregar_vacunacion.html` con las variables contextuales
    formulario' y 'mascota'.
    """
    mascota = Mascota.objects.get(id=mascota_id)

    if request.method == 'POST':
        form = VacunacionForm(request.POST, request.FILES)
        if form.is_valid():
            vacunacion = form.save(commit=False)
            vacunacion.mascota = mascota  # Asignar la mascota relacionada
            vacunacion.save()
            return redirect('infomascotas', mascota_id=mascota_id)
    else:
        form = VacunacionForm()

    context = {
        'form': form,
        'mascota': mascota
    }
    return render(request, 'mascotas/agregar_vacunacion.html',context)

def agregar_atencion(request, mascota_id):
    """
    La función "agregar_atencion" añade un nuevo objeto "Atencion" a un objeto "Mascota" específico y
    redirige a la página de "infomascotas".
    
    :param petición: El objeto request representa la petición HTTP realizada por el usuario. Contiene
    información como la sesión del usuario, el método HTTP utilizado (GET, POST, etc.), y cualquier dato
    enviados con la solicitud
    param mascota_id: El parámetro `mascota_id` es el ID de la mascota para la que se está añadiendo la atencion
    (cuidado). Se utiliza para recuperar el objeto mascota específico de la base de datos.
    :devuelve: una plantilla HTML renderizada llamada `mascotas/agregar_atencion.html` con las variables de contexto
    'formulario' y 'mascota'.
    """
    mascota = Mascota.objects.get(id=mascota_id)

    if request.method == 'POST':
        form = AtencionForm(request.POST, request.FILES)
        if form.is_valid():
            atencion = form.save(commit=False)
            atencion.mascota = mascota  # Asignar la mascota relacionada
            atencion.save()
            return redirect('infomascotas', mascota_id=mascota_id)
    else:
        form = AtencionForm()

    context = {
        'form': form,
        'mascota': mascota
    }
    return render(request, 'mascotas/agregar_atencion.html', context)


def agregar_desparacitacion(request, mascota_id):
    """
    La función `agregar_desparacitacion` añade un registro de desparacitación para una mascota dada.
    
    :param petición: El parámetro `request` es un objeto que representa la petición HTTP realizada por el
    cliente. Contiene información como el método de petición (GET, POST, etc.), cabeceras, sesión de usuario,
    y cualquier dato enviado con la petición
    :param mascota_id: El parámetro `mascota_id` es el ID de la mascota para la que queremos
    añadir un registro de desparasitación
    :return: una plantilla HTML renderizada con el formulario y el objeto mascota como variables de contexto.
    """
    mascota = Mascota.objects.get(id=mascota_id)

    if request.method == 'POST':
        form = DesparacitacionForm(request.POST, request.FILES)
        if form.is_valid():
            desparacitacion = form.save(commit=False)
            desparacitacion.mascota = mascota  # Asignar la mascota relacionada
            desparacitacion.save()
            return redirect('infomascotas', mascota_id=mascota_id)
    else:
        form = DesparacitacionForm()

    context = {
        'form': form,
        'mascota': mascota
    }
    return render(request, 'mascotas/agregar_desparacitacion.html', context)