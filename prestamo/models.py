from django.db import models

# Create your models here.
class Prestamo(models.Model):
    id=models.AutoField(primary_key=True)
    matricula=models.CharField(max_length=20, verbose_name='Matricula',unique=True)
    equipo_id=models.IntegerField(default='0',null=True,verbose_name='Equipo')
    fecha_prestamo=models.DateTimeField(null=True,verbose_name='Fecha Prestamo')
    status=models.IntegerField(default='0',null=True,verbose_name='status')
    oportunidad=models.IntegerField(default='0',null=True,verbose_name='oportunidad')
    fecha_entrega=models.DateTimeField(null=True,verbose_name='Fecha Entrega')