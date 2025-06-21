from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile,Mascota,Vacunacion,Desparacitacion,Atencion
from django.db.models import FileField

# El código anterior define varias clases admin para diferentes modelos en un proyecto Django, cada uno con
# visualización de listas, campos de búsqueda y filtros específicos.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'rut_user', 'address', 'location', 'telephone', 'user_group')
    search_fields = ('user__username', 'location', 'user__groups__name')
    list_filter = ('user__groups__name', 'location')

    def username(self, obj):
        return obj.user.username

    def user_group(self, obj):
        return " - ".join([t.name for t in obj.user.groups.all().order_by('name')])

    username.short_description = 'Nombre de usuario'
    user_group.short_description = 'Grupo'

admin.site.register(Profile, ProfileAdmin)

# La clase `MascotaAdmin` es una subclase de `admin.ModelAdmin` que define las opciones de visualización, filtrado,
# y opciones de búsqueda para el modelo `Mascota` en el sitio de administración de Django.
class MascotaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo_mascota', 'edad', 'sexo', 'color', 'fecha_nacimiento', 'raza', 'rut_user']
    list_filter = ['tipo_mascota', 'sexo', 'raza']
    search_fields = ['nombre', 'color']
    
admin.site.register(Mascota, MascotaAdmin)

class VacunacionAdmin(admin.ModelAdmin):
    list_display = ['nombre_vacuna', 'tipo_vacuna', 'documento', 'mascota']
    fields = ['nombre_vacuna', 'tipo_vacuna', 'documento', 'mascota']
    list_filter = ['tipo_vacuna']
    search_fields = ['nombre_vacuna', 'tipo_vacuna']
    def save_model(self, request, obj, form, change):
        # Guarda una referencia al archivo antes de eliminar el objeto
        file = obj.documento
        super().save_model(request, obj, form, change)
        # Verifica si el objeto se eliminó y si el archivo adjunto existe
        if change and not obj.documento and isinstance(file, FileField) and file:
            file.delete()

admin.site.register(Vacunacion,VacunacionAdmin)

class DesparacitacionAdmin(admin.ModelAdmin):
    list_display = ['nombre_desparacitacion', 'tipo_desparacitacion', 'mascota']
    list_filter = ['tipo_desparacitacion']
    search_fields = ['nombre_desparacitacion', 'tipo_desparacitacion']
    def save_model(self, request, obj, form, change):
        # Guarda una referencia al archivo antes de eliminar el objeto
        file = obj.documento
        super().save_model(request, obj, form, change)
        # Verifica si el objeto se eliminó y si el archivo adjunto existe
        if change and not obj.documento and isinstance(file, FileField) and file:
            file.delete()
admin.site.register(Desparacitacion,DesparacitacionAdmin)

class AtencionAdmin(admin.ModelAdmin):
    list_display = ['nombre_atencion', 'tipo_atencion', 'mascota']
    list_filter = ['tipo_atencion']
    search_fields = ['nombre_atencion', 'tipo_atencion']
    def save_model(self, request, obj, form, change):
        # Guarda una referencia al archivo antes de eliminar el objeto
        file = obj.documento
        super().save_model(request, obj, form, change)
        # Verifica si el objeto se eliminó y si el archivo adjunto existe
        if change and not obj.documento and isinstance(file, FileField) and file:
            file.delete()
admin.site.register(Atencion,AtencionAdmin)
