from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests

def index(request):
    return render(request, 'index.html')

def primerPunto(request):
    return  render(request, 'primero.html')

def segundoPunto(request):
    numero = request.GET.get('numero')
    x=numero+numero
    data = {'allright': x}
    return JsonResponse(data)

def tercerPunto(request):
    return  render(request, 'tercero.html')

def cuartoPunto(request):
    return  render(request, 'cuarto.html')

def varias(request):
    numero = request.GET.get('numero')
    nombre = request.GET.get('nombre')
    data = {'allright': numero,'allright2': nombre}
    return JsonResponse(data)

def texto(request):
    numero = request.GET.get('numero')
    nombre = request.GET.get('nombre')
    x="La persona "+str(nombre)+" tiene "+str(numero)+" años"
    data = {'allright': x}
    return JsonResponse(data)

def quintoPunto(request):
    return  render(request, 'quinto.html')

def sextoPunto(request):
    return  render(request, 'sexto.html')

def septimoPunto(request):
    return  render(request, 'septimo.html')

def octavoPunto(request):
    return  render(request, 'octavo.html')

def peticion(request):
    numero = request.GET.get('numero')
    nombre = request.GET.get('nombre')
    payload = {'numero': numero, 'nombre': nombre}
    r = requests.post('http://localhost:8080/', params=payload)
    data = {'allright': True}
    return JsonResponse(data)



