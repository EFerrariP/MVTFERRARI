from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render

def index(request):
    datos = {"Familiares":["Roberto"]}
    doc = loader.get_template("index.html")
    documento = doc.render(datos)
    return HttpResponse(documento)