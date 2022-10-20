from email.policy import default
from enum import unique
from django.db import models

# Create your models here.
class Docentes(models.Model):
    id=models.AutoField(primary_key=True)
    matricula=models.CharField(max_length=20, verbose_name='Matricula',unique=True)
    nombre=models.CharField(max_length=100, verbose_name='Nombre')
    apellido=models.CharField(max_length=100, verbose_name='Apellido')
    correo=models.EmailField(max_length=100, verbose_name='Correo')
    imagen=models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    status=models.IntegerField(default='0',null=True,verbose_name='status')
    n_sancion=models.IntegerField(default='0',null=True,verbose_name='Numero de Sanciones')
    duracion_sancion=models.DateTimeField(null=True,verbose_name='Duración de sancion')

    def delete(self,using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()