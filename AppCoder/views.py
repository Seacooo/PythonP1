from django.shortcuts import render
from AppCoder.models import Curso
# Create your views here.
def inicio(request):
    return render(request, "AppCoder/inicio.html")

def curso(request):
    return render(request, "AppCoder/curso.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

def cursoFormulario(request):
      if request.method == 'POST':
      
            curso =  Curso(nombre=request.POST['curso'],camada=request.POST['camada'])
 
            curso.save()
 
            return render(request, "AppCoder/inicio.html")
 
      return render(request,"AppCoder/cursoFormulario.html")