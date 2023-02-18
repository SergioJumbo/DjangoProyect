from django.db import models

from app import settings


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

class Carrera(models.Model):
    id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    nombre = models.CharField(max_length=300, null=False)
    facultad = models.ForeignKey(Facultad, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'Carreras'
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'
        ordering = ['id']

class Matricula(models.Model):
    id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.fechaInicio)

    class Meta:
        db_table = 'Matriculas'
        verbose_name = 'Matricula'
        verbose_name_plural = 'Matriculas'
        ordering = ['id']

class Ciclo(models.Model):
    id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    numero = models.IntegerField(null=False)
    carrera = models.ForeignKey(Carrera, on_delete=models.RESTRICT)
    matricula = models.ForeignKey(Matricula, on_delete=models.RESTRICT)

    def __str__(self):
        return str(self.numero)

    class Meta:
        db_table = 'Ciclos'
        verbose_name = 'Ciclo'
        verbose_name_plural = 'Ciclos'
        ordering = ['id']

class Persona(models.Model):
    nombre = models.CharField(max_length=300, null=False)
    edad = models.IntegerField(null=False)

    class Meta:
        abstract = True

class Docente(Persona):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'Docentes'
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'
        ordering = ['id']

class Asignatura(models.Model):
    id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    nombre = models.CharField(max_length=300, null=False)
    ciclo = models.ForeignKey(Ciclo, on_delete=models.RESTRICT)
    docente = models.ForeignKey(Docente, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'Asignaturas'
        verbose_name = 'Asignatura'
        verbose_name_plural = 'Asignaturas'
        ordering = ['id']

class Estudiante(Persona):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    asignatura = models.ManyToManyField(Asignatura)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'Estudiantes'
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
        ordering = ['id']


class RegistroAsistencia(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    fecha = models.DateField()
    estudiante = models.ForeignKey(Estudiante, on_delete=models.RESTRICT)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.RESTRICT)

    def __str__(self):
        return str(self.fecha)

    class Meta:
        db_table = 'RegistroAsistencias'
        verbose_name = 'RegistroAsistencia'
        verbose_name_plural = 'RegistroAsistencias'
        ordering = ['id']