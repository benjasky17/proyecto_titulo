from django import forms
from accounts.models import Profile,Mascota,Vacunacion,Desparacitacion,Atencion


# The code defines several form classes for different models in a Python application.
# La clase `PerfilForm` es un formulario que se utiliza para actualizar los campos de un modelo `Profile`, con etiquetas # personalizadas para cada campo.
# personalizadas para cada campo.
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['rut_user','address','location','telephone']
        labels = {
            'rut_user': 'rut',
            'address': 'Dirección',
            'location': 'Comuna',
            'telephone': 'Teléfono'
        }


# La clase `MascotaForm1` es una subclase de `forms.ModelForm` que define un formulario para crear o
# actualizar instancias del modelo `Mascota`, con campos y etiquetas específicas.
class MascotaForm1(forms.ModelForm):
   
    
    class Meta:
        model = Mascota
        fields = ['tipo_mascota', 'nombre', 'edad', 'sexo', 'color', 'fecha_nacimiento', 'raza']
        labels = {
            'tipo_mascota': 'Tipo',
            'nombre': 'Nombre mascota',
            'edad': 'Edad',
            'sexo': 'Sexo',
            'color': 'Color de la mascota',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'raza': 'Raza'
        }




# La clase VacunacionForm es un ModelForm que especifica los campos a incluir en el formulario para el
# modelo Vacunacion.
class VacunacionForm(forms.ModelForm):
    class Meta:
        model = Vacunacion
        fields = ['nombre_vacuna', 'tipo_vacuna', 'documento']



# La clase DesparacitacionForm es un formulario que se utiliza para crear o actualizar instancias del modelo de
# modelo de Desparacitación.
class DesparacitacionForm(forms.ModelForm):
    class Meta:
        model = Desparacitacion
        fields = ['nombre_desparacitacion', 'tipo_desparacitacion', 'documento']

# La clase AtencionForm es un ModelForm que especifica los campos a incluir en el formulario para el
# modelo Atencion.
class AtencionForm(forms.ModelForm):
    class Meta:
        model = Atencion
        fields = ['nombre_atencion', 'tipo_atencion', 'documento']