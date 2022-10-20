from django.db import models

class Equipos(models.Model):
    id=models.AutoField(primary_key=True)
    imagen=models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    nombre=models.CharField(max_length=100, verbose_name='Nombre')
    codigo=models.CharField(max_length=100, verbose_name='Codigo')
    status=models.IntegerField(default='0',null=True,verbose_name='Status')
    categoria=models.IntegerField(default='0',verbose_name='Categoria')
    
    def delete(self,using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()