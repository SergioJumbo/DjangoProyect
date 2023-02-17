from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from asistencias.models import Universidad


def login(request):
    data = {
        'nombre':'Sergio',
        'u': Universidad.objects.all()[0].nombre
    }
    return JsonResponse(data)

def logDocente(request):
    data = {
        'tipo':'docente',
        'nombre':'roberto',
        'universidad': Universidad.objects.all()[0].nombre
    }
    return JsonResponse(data)

def logEstudiante(request):
    data = {
        'tipo':'estudiante',
        'nombre':'sergio',
        'universidad': Universidad.objects.all()[0].nombre
    }
    return JsonResponse(data)