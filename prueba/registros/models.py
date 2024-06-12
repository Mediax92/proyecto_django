from django.db import models

# Create your models here.

class Alumnos(models.Model):#Define la estructura de nuestra tabla
    matricula = models.CharField(max_length=12, verbose_name="Mat")#texto corto
    nombre = models.TextField()#Texto largo
    carrera = models.TextField()
    turno = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Crear")#Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Actualizar")

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ["-created"]
        #el menos indica que se ordenara del más reciente al mas viejo

    def __str__(self):
        return self.nombre
        #indica que se mostrara el nombre como valor en la tabla