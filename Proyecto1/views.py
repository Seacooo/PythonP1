from django.http import HttpResponse
from django.template import Template, Context
import datetime
from django.template import loader

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def segunda_vista(request):
    return HttpResponse ("<br>Ya entendimos esto,<br> es muy simple")

def DiaDeHoy(request):
    dia = datetime.datetime.now()
    DocumentoDeTexto = f"hoy es el dia {dia}"
    return HttpResponse (DocumentoDeTexto)

def MiNombreEs(self, nombre):
    DocumentoDeTexto= f"Mi Nombre Es <br> <br> {nombre}"
    return HttpResponse (DocumentoDeTexto)

def ProbandoTemplate(self):

    nom= "Marco"
    ap= "Coppola"
    lista_notas=[2,3,5,4,2]

    diccionario= {"nombre":nom, "apellido":ap, "notas":lista_notas}

    

    #miHtml= open("C:/Users/Usuario/OneDrive/Escritorio/v/Programacion/Portfolio parte 1/PythonP1/Proyecto1/Proyecto1/Plantillas/template1.html")
    
    #plantilla= Template(miHtml.read())

    #miHtml.close()

    #miContext= Context(diccionario)

    #documento= plantilla.render(miContext)

    plantilla= loader.get_template("template1.html")

    documento= plantilla.render(diccionario)

    return HttpResponse (documento)

