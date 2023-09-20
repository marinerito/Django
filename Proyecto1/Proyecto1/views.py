from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola")

def diaDeHoy(request):
    dia = datetime.datetime.now()

    documentoDeTexto = f"hoy es <br> {dia}"

    return HttpResponse(documentoDeTexto)

def edad(self, edad):

    e = "tengo " + edad

    return HttpResponse(e)

def probandoTemplates(request):
    miHtml = open("C:/Users/giova/Downloads/Python/PythonProyecto1/Proyecto1/plantillas/plantilla1.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)

    return HttpResponse(documento)

