from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre_1 = models.CharField(max_length=100)
    nombre_2 = models.CharField(max_length=100, blank=True, null=True)
    apellido_1 = models.CharField(max_length=100)
    apellido_2 = models.CharField(max_length=100, blank=True, null=True)
    codigo_estudiantil = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.nombre_1} {self.nombre_2} {self.apellido_1} {self.apellido_2} ({self.codigo_estudiantil})"

class Dia(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class BeneficiadoPorDia(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    dia_beneficiado = models.ForeignKey(Dia, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.estudiante} - {self.dia_beneficiado}"

class FilaVirtual(models.Model):
    turno = models.IntegerField()
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"Fila Virtual - {self.estudiante} - {self.turno}"
