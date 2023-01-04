from django.shortcuts import render

# Create your views here.
def layout(request):
    return render (request, 'layout.html')

def ruta_saludo(request):
    return render (request,'saludo.html')

def ruta_integrantes(request):
    return render (request,'integrantes.html')