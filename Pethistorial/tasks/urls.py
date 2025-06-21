"""
URL configuration for prettytails project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from tasks.views import home, exit, register, nosotros,Perfil, NMascotas, infomascotas, agregarMascota, agregar_desparacitacion, agregar_vacunacion, agregar_atencion
from accounts.views import agregarPerfil
from django.conf import settings
from django.conf.urls.static import static,serve

# La lista `urlpatterns` se utiliza para mapear URLs a vistas en el framework web Django. Cada llamada a la función `path`
# representa un patrón de URL y especifica la función de vista correspondiente que debe ser
# cuando se accede a esa URL.

urlpatterns = [
   path('', home, name='home'),
   path('login/', exit, name='exit'),
   path('logout/', exit, name='exit'),
   path('register/', register, name='register'),
   path('nosotros/', nosotros, name='nosotros'),
   path('NMascotas/', NMascotas, name='NMascotas'),
   path('agregar_vacunacion/<int:mascota_id>/', agregar_vacunacion, name='agregar_vacunacion'),
   path('mascotas/<int:mascota_id>/', infomascotas, name='infomascotas'),
   path('Perfil/', Perfil, name='Perfil'),
   path('agregarPerfil/', agregarPerfil, name='agregarPerfil'),
   path('agregarMascota/', agregarMascota, name='agregarMascota'),
   path('agregar_atencion/<int:mascota_id>/', agregar_atencion, name='agregar_atencion'),
   path('agregar_desparacitacion/<int:mascota_id>/', agregar_desparacitacion, name='agregar_desparacitacion'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


