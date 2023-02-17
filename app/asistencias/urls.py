
from django.urls import path

from asistencias.views import login, logDocente, logEstudiante
urlpatterns = [
    path('docente/', logDocente),
    path('estudiante/', logEstudiante)
]