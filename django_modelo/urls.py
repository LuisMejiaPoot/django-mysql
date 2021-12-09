"""django_modelo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from alumnos.views  import * 

urlpatterns = [
    path('admin/', admin.site.urls),

    path("alumnos",alumnos, name="alumnos"),
    path("vista-alumnos",viewAlumnos,name="vistaAlumnos"),
    path("ver-alumno/<matricula>",view_update_alumno,name="ver_alumno"),
    path("agregar-alumno",agregar_alumno_form,name="agregar_usuario"),
    path("agregar-alumno-add",agregar_alumno,name="add_alumno"),
    path("eliminar-alumno/<id_alumno>",delete_alumnos,name="delete_alumno")

]
