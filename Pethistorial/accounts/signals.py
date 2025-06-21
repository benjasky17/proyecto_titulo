from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile

@receiver(post_save, sender=Profile)    
def add_user_to_users_group(sender, instance, created, **kwargs):
    """
    Esta función añade una instancia de Perfil recién creada al grupo 'Cliente'.
    
    param remitente: El parámetro `sender` se refiere a la clase modelo que está enviando la señal. En este
    caso, es el modelo `Profile
    :param instancia: El parámetro "instance" hace referencia a la instancia del modelo Profile que se acaba de
    guardado. En otras palabras, representa el objeto Profile específico que activó la señal post_save.
    :param creado: El parámetro `created` es un valor booleano que indica si se ha creado una nueva instancia del modelo `Profile`.
    del modelo `Profile` o se ha actualizado una instancia existente. Es `True` si se ha creado una nueva instancia
    y `False` si se ha actualizado una instancia existente.
    """
    if created:
        try:
            users = Group.objects.get(name='Cliente')
        except Group.DoesNotExist:
            users = Group.objects.create(name='Administrativo')
            users = Group.objects.create(name='Cliente')
            users = Group.objects.create(name='Veterinario')            
        instance.user.groups.add(users)