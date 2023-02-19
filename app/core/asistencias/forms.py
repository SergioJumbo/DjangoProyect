from django.contrib.admin.widgets import AdminDateWidget
from django.forms import *

from core.asistencias.models import RegistroAsistencia


class RegistroAsistenciaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        # user_id = kwargs.pop('user_id', None)
        # print(user_id)
        # print(self.request.user.id)
        self.initial['estudiante'] = self.user.estudiante.id
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


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.instance.estudiante_id = 1
    # def __init__(self, *args, **kwargs):
    #     super(RegistroAsistenciaForm, self).__init__(*args, **kwargs)
    #     print(self.request.user.id)
    #     self.initial['estudiante'] = 1
        #self.initial['estudiante'] = self.request.user.estudiante