from django.shortcuts import render

from core.asistencias.models import RegistroAsistencia


def reporte_list(request):
    data = {
        'title':'Reporte de Asistencias',
        'reporte': RegistroAsistencia.objects.all()
    }
    return render(request, 'reporte/list.html', data)