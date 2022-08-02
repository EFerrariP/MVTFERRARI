from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render

    archivo = open(r"C:\Users\Michifu\AppData\Local\Programs\Python\Python310\Scripts\MVTFERRARI\MVTFERRARI\templates\index.html", "r")
    contenido_html = archivo.read()
    archivo.close()  
    plantilla = Template(contenido_html)
    contexto = Context(datos_contexto) 
    documento_a_renderizar = plantilla.render(contexto)
    return HttpResponse(documento_a_renderizar) 