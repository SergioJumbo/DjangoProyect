from django.conf.global_settings import MEDIA_URL, STATIC_URL
from django.contrib.auth.models import AbstractUser
from django.db import models

from core.asistencias.models import Estudiante

class Usuario(AbstractUser):
    #image = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)
    #direccion: models.CharField(max_length=300)
    #estudiante: models.ForeignKey(Estudiante, on_delete=models.RESTRICT, null=True, blank=True)
    #estudiante_id = models.IntegerField(blank=True, null=True)
    # def __str__(self):
    #     return self.direccion

    # def get_image(self):
    #     if self.image:
    #         return '{}{}'.format(MEDIA_URL, self.image)
    #     return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        db_table = 'Usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['id']

