
from django.urls import path
from core.asistencias.views.reporte.view import reporte_list

urlpatterns = [
    path('student/report/', reporte_list, name= 'reporte_list')
]