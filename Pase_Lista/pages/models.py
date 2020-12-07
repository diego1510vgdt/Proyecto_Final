from django.db import models

# Create your models here.

#Modelo del alumno
class Alumno(models.Model):
    nombre = models.CharField(max_length = 150)
    
    def __str__(self):
        return self.nombre

#Modelo de materia
class Materia(models.Model):
    nombre = models.CharField(max_length = 60)
    periodo = models.CharField(max_length = 20)
    year = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.nombre

#Modelo de clase
class Clase(models.Model):
    dias_clase = models.CharField(max_length=70)
    hora_ini = models.TimeField()
    hora_fin = models.TimeField()
    grupo = models.CharField(max_length=10, default = '')
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, default=0)
    extras = models.CharField(max_length = 800)
    
    def __str__(self):
        return self.nombre

#Modelo del profesor
class Profesor(models.Model):
    nombre = models.CharField(max_length = 30)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

#Modelo de asistencias
class Asistencia(models.Model):
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, default=0)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.fecha_creacion