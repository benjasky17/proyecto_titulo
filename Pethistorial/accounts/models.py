from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
from django.urls import reverse

class Profile(models.Model):
    """
    El código anterior define un modelo de Perfil con campos para la información del usuario y crea un perfil para
    cada usuario cuando se crea.
    
    :param remitente: El parámetro "sender" en el código se refiere a la clase de modelo que está enviando la
    señal. En este caso, el emisor es el modelo User
    :param instancia: El parámetro "instance" se refiere a la instancia del modelo de usuario que se está guardando o creando.
    está guardando o creando. En este caso, representa el objeto usuario
    :param creado: El parámetro "created" es un valor booleano que indica si se ha creado una nueva instancia del modelo
    se ha creado una nueva instancia del modelo de usuario o se ha actualizado una instancia existente.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    rut_user = models.IntegerField(null=True, blank=True, verbose_name='Rut')
    address = models.CharField(max_length=50, null=True, blank=True, verbose_name='Dirección')
    location = models.CharField(max_length=50, null=True, blank=True, verbose_name='Comuna')
    telephone = models.CharField(max_length=50, null=True, blank=True, verbose_name='Teléfono')

    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'
        ordering = ['-id']

    def __str__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)

# La clase anterior define un modelo para una mascota, con varios atributos como tipo, nombre, edad, sexo,
# color, fecha de nacimiento, raza, y una clave externa a un perfil de usuario.
class Mascota(models.Model):
    tipo_mascota = models.CharField(max_length=20)
    nombre = models.CharField(max_length=30,null=False,  verbose_name='nombre mascota')
    edad = models.IntegerField(null=False, verbose_name='edad')
    sexo = models.CharField(max_length=20,null=False, verbose_name='sexo')
    color = models.CharField(max_length=30,null=False,  verbose_name='color mascota')
    fecha_nacimiento = models.DateField(null=False,  verbose_name='fecha_nacimiento')
    raza = models.CharField(max_length=30,null=False, verbose_name='raza')
    rut_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='rut')

    def __str__(self):
        return self.nombre
    
# La clase Vacunacion representa un registro de vacunacion para una mascota, incluyendo el nombre de la vacuna,
# el tipo de vacuna, y un documento opcional asociado a la vacuna.
class Vacunacion(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    nombre_vacuna = models.CharField(max_length=100)
    tipo_vacuna = models.CharField(max_length=100)
    documento = models.FileField(upload_to='infomascotas/',null=True)
    def get_documento_url(self):
        if self.documento:
            return settings.MEDIA_URL + str(self.documento)
        return ''
    
    def __str__(self):
        return self.nombre_vacuna
    
# La clase `Desparacitacion` representa un modelo para registros de desparasitacion de una mascota, con campos
# para la mascota, nombre de la desparasitacion, tipo de desparasitacion, y un archivo de documento.
class Desparacitacion(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    nombre_desparacitacion = models.CharField(max_length=100)
    tipo_desparacitacion = models.CharField(max_length=100)
    documento = models.FileField(upload_to='infomascotas/',null=True)
    def get_documento_url(self):
        if self.documento:
            return settings.MEDIA_URL + str(self.documento)
        return ''
    
    def __str__(self):
        return self.nombre_desparacitacion

# La clase `Atencion` representa un modelo para la atención de una mascota, con atributos como la mascota, el
# nombre de la atención, el tipo de atención, y un documento asociado a la atención.
class Atencion(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    nombre_atencion = models.CharField(max_length=100)
    tipo_atencion = models.CharField(max_length=100)
    documento = models.FileField(upload_to='infomascotas/',null=True)
    def get_documento_url(self):
        if self.documento:
            return settings.MEDIA_URL + str(self.documento)
        return ''
    
    def __str__(self):
        return self.nombre_atencion