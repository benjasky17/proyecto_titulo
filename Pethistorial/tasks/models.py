from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Recordatorio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recordatorios_tasks')
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_recordatorio = models.DateField()
    

    def __str__(self):
        return f"{self.titulo} - {self.fecha_recordatorio}"
    
    