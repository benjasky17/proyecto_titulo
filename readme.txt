python manage.py createsuperuser
usuario admin
correo admin@admin.cl
password admin



https://dev.mysql.com/downloads/mysql/

Windows (x86, 64-bit), MSI Installer	9.3.0	169.5M	 Download

recomendacion instalar workbench
https://downloads.mysql.com/archives/workbench/
 
Windows (x86, 64-bit), MSI Installer	Jan 10, 2025	42.0M	Download

base datos creada ahi "PetHistorial"
usuario "admin" 
password "admin"



PASOS PARA CREAR Y ACTIVAR UN ENTORNO VIRTUAL EN WINDOWS

1. Abre la terminal (CMD o PowerShell) en la carpeta del proyecto.

2. Ejecuta el siguiente comando para crear el entorno virtual:
   python -m venv venv

3. Activa el entorno virtual con:
   .\venv\Scripts\activate

4. Instala las dependencias del proyecto:
   pip install -r requirements.txt

   python manage.py migrate

   python manage.py runserver

5. Para desactivar el entorno virtual, usa:
   deactivate 

   