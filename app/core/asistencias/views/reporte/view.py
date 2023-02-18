from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
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

        return JsonResponse(data)
    def get_queryset(self):
        return RegistroAsistencia.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte de Asistencias'
        context['create_url'] = reverse_lazy('reporteCreate')
        context['list_url'] = reverse_lazy('reporteList')
        context['entity'] = 'Asistencias'
        return context

class ReporteCreateView(CreateView):
    model= RegistroAsistencia
    form_class = RegistroAsistenciaForm
    template_name = 'reporte/create.html'
    success_url = reverse_lazy('reporteList')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registrar Asistencia'
        context['entity'] = 'Asistencias'
        context['list_url'] = reverse_lazy('reporteList')
        context['action'] = 'add'
        return context

class ReporteUpdateView(UpdateView):
    model = RegistroAsistencia
    form_class = RegistroAsistenciaForm
    template_name ='reporte/create.html'
    success_url =reverse_lazy('reporteList')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Asistencia'
        context['entity'] = 'Asistencias'
        context['list_url'] = reverse_lazy('reporteList')
        context['action'] = 'edit'
        return context

class ReporteDeleteView(DeleteView):
    model = RegistroAsistencia
    template_name ='reporte/delete.html'
    success_url =reverse_lazy('reporteList')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Asistencia'
        context['entity'] = 'Asistencias'
        context['list_url'] = reverse_lazy('reporteList')
        context['action'] = 'edit'
        return context