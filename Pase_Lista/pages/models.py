from django.db import models

# Create your models here.

#Modelo del alumno
class Alumno(models.Model):
    nombre = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.nombre

#Modelo de asistencias
class Asistencia(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.fecha_creacion

#Modelo de clase
class Clase(models.Model):
    dias_clase = models.DateField(auto_now_add = True)
    hora_ini = models.TimeField()
    hora_fin = models.TimeField()
    asis = models.ForeignKey(Asistencia, on_delete=models.CASCADE)
    extras = models.CharField(max_length = 800)
    
    def __str__(self):
        return self.nombre

#Modelo de materia
class Materia(models.Model):
    nombre = models.CharField(max_length = 30)
    periodo = models.CharField(max_length = 30)
    year = models.CharField(max_length = 30)
    cla = models.ForeignKey(Clase, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

#Modelo del profesor
class Profesor(models.Model):
    nombre = models.CharField(max_length = 30)
    mat = models.ForeignKey(Materia, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre