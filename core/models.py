from django.db import models

# Create your models here.

class Paises(models.Model):
    idPais = models.IntegerField(primary_key=True, verbose_name='id de País')
    nombrePais = models.CharField(max_length= 100, verbose_name='nombre de País')

    def __str__(self):
        return self.nombrePais

class Colaborador(models.Model):
    rutColaborador = models.CharField(primary_key=True, max_length= 10, verbose_name='Rut de Colaborador')
    imagen = models.ImageField(upload_to='media/colaborador/', null=True, blank=True)
    nombreCompleto = models.CharField(max_length= 200, verbose_name='Nombre Completo')
    telefono = models.CharField(max_length= 12, verbose_name='Teléfono')
    direccion = models.CharField(max_length= 200, verbose_name='Dirección')
    email = models.CharField(max_length= 200, verbose_name='Email')
    pais = models.ForeignKey(Paises, on_delete=models.CASCADE)
    contraseña = models.CharField(max_length= 200, verbose_name='Contraseña')

    def __str__(self):
        return self.rutColaborador