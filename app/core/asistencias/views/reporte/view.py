from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator

from core.asistencias.forms import RegistroAsistenciaForm
from core.asistencias.models import RegistroAsistencia


# def reporte_list(request):
#     data = {
#         'title':'Reporte de Asistencias',
#         'reporte': RegistroAsistencia.objects.all()
#     }
#     return render(request, 'reporte/list.html', data)

class ReporteListView(ListView):
    model = RegistroAsistencia
    template_name = 'reporte/list.html'
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = RegistroAsistencia.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)

        print(request.POST)
        #print(regAsis)
        #data['fecha'] = regAsis.fecha
        return JsonResponse(data)
    def get_queryset(self):
        return RegistroAsistencia.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte de Asistencias'
        return context

class ReporteCreateView(CreateView):
    model= RegistroAsistencia
    form_class = RegistroAsistenciaForm
    template_name = 'reporte/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registrar Asistencia'
        return context