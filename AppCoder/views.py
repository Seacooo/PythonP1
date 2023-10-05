from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse("inicio")

def curso(request):
    return HttpResponse("Hola curso")

def profesores(request):
    return HttpResponse("Hola profesores")

def estudiantes(request):
    return HttpResponse("Hola estudiantes")

def entregables(request):
    return HttpResponse("entregables")
