
from django.urls import path

from core.asistencias.views import logDocente, logEstudiante
urlpatterns = [
    path('docente/', logDocente),
    path('estudiante/', logEstudiante)
]