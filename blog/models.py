from django.db import models
from .validators import validate_edad, validate_capacity, validate_email

# Create your models here.

class Taller(models.Model):
    nombre = models.CharField(max_length=80, unique= True)
    capacidad = models.IntegerField(
         default=20,
         validators=[validate_capacity]
         )
    descripcion = models.TextField()

    def __str__(self):
         return self.nombre

class nivelEstudiante(models.TextChoices):
    BASICO = 'básico','BASICO'
    INTERMEDIO = 'intermedio','INTERMEDIO'
    AVANZADO = 'avanzado','AVANZADO'

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveBigIntegerField(validators=[validate_edad])
    email = models.CharField(max_length=100, unique=True, validators=[validate_email])
    nivel = models.CharField(
        max_length= 10,
        choices= nivelEstudiante.choices,
        default= nivelEstudiante.BASICO
    )
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
         return self.nombre

class inscripcion(models.Model):
    taller = models.ForeignKey(Taller, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

class tipoArchivo(models.TextChoices):
       PDF = 'pdf','PDF'
       VIDEO = 'video', 'VIDEO'
       IMAGEN = 'imagen', 'IMAGEN'
   
class material(models.Model):
    taller = models.ForeignKey(Taller, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField
    tipo_de_archivo = models.CharField(
        max_length= 10,
        choices=tipoArchivo.choices,
        default= tipoArchivo.PDF
    )
    archivo = models.FileField(upload_to='recursos/')