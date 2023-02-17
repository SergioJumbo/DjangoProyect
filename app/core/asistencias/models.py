from django.db import models

# Create your models here.

class Universidad(models.Model):
    id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    nombre = models.CharField(max_length=300, null=False)
    direccion = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table='Universidades'
        verbose_name='Universidad'
        verbose_name_plural='Universidades'
        ordering=['id']

class Facultad(models.Model):
    id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    nombre = models.CharField(max_length=300, null=False)
    universidad = models.ForeignKey(Universidad, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'Facultades'
        verbose_name = 'Facultad'
        verbose_name_plural = 'Facultades'
        ordering = ['id']