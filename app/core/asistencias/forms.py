from django.contrib.admin.widgets import AdminDateWidget
from django.forms import *
from core.asistencias.models import RegistroAsistencia

class RegistroAsistenciaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        try:
            self.estudiante = kwargs.pop('estudiante')
        except:
            print("warning")

        super().__init__(*args, **kwargs)
        try:
            self.initial['estudiante'] = self.estudiante.id
        except:
            print("warning")

        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
            if form.field.label == 'Estudiante':
                form.field.disabled = True

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

