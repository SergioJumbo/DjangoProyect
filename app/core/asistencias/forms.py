from django.forms import ModelForm

from core.asistencias.models import RegistroAsistencia


class RegistroAsistenciaForm(ModelForm):
    class Meta:
        model = RegistroAsistencia
        fields = '__all__'
