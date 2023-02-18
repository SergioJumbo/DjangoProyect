from django.contrib.admin.widgets import AdminDateWidget
from django.forms import *

from core.asistencias.models import RegistroAsistencia


class RegistroAsistenciaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = RegistroAsistencia
        fields = '__all__'
        labels = {
            'fecha':'Fecha de asistencia'
        }
        widgets = {
            'fecha': DateInput(
            attrs={
                'type': 'date',
                'placeholder': 'mm-dd-yyyy'
                },
            format = '%Y-%m-%d'
            )

        }