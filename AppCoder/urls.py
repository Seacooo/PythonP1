"""
URL configuration for Proyecto1 project.

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
from django.contrib import admin
from django.urls import path
from AppCoder import views

urlpatterns = [
    path("inicio/", views.inicio, name="Inicio"),
    path("estudiantes/", views.estudiantes, name= "Estudiantes"),
    path("profesores/", views.profesores, name="Profesores"),
    path("curso/", views.curso, name="Cursos"),
    path("entregables/", views.entregables, name="Entregables"),
    path("cursoform/", views.cursoFormulario, name="cursoForm"),
    path("apicursoform/", views.apiCursoFormulario, name="apiCursoForm"),
    path("buscar/", views.buscar, name="Buscar"),
    path("mostrar/", views.mostrar, name="Mostrar"),
]
