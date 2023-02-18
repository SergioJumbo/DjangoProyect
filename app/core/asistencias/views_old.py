from django.shortcuts import render
from django.http import JsonResponse

from core.asistencias.models import Universidad

def home(request):
    data = {
        'universidad': Universidad.objects.first()
    }
    return render(request, 'home.html', data)

def login(request):
    data = {
        'title' : 'Iniciar sesión',
        'nombre':'Sergio',
        'u': Universidad.objects.all()[0].nombre
    }
    return render(request, 'login.html', data)

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