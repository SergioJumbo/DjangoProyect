
from django.urls import path
from core.asistencias.views.reporte.view import ReporteListView, ReporteCreateView, ReporteUpdateView

urlpatterns = [
    path('student/report/', ReporteListView.as_view(), name= 'reporteList'),
    path('student/create/', ReporteCreateView.as_view(), name= 'reporteCreate'),
    path('student/edit/<int:pk>/', ReporteUpdateView.as_view(), name= 'reporteUpdate')
]