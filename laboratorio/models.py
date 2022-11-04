from django.db import models

# Create your models here.
class Laboratorios(models.Model):
    id=models.AutoField(primary_key=True)
    imagen=models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    nombre=models.CharField(max_length=100, verbose_name='Nombre')
    status=models.IntegerField(default='0',null=True,verbose_name='Status')
    
    def delete(self,using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()