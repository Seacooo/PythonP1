from django.shortcuts import render
from AppCoder.models import Curso
from AppCoder.forms import CursoFormulario
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

def apiCursoFormulario(request):
     
    if request.method == "POST":
 
        miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
                  curso.save()
                  return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = CursoFormulario()
 
    return render(request, "AppCoder/apiCursoFormulario.html", {"miFormulario": miFormulario})