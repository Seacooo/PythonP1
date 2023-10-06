from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola Bienvenido")