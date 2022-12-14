# Generated by Django 4.1.2 on 2022-10-14 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docentes', '0006_delete_equipos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imagen', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('codigo', models.CharField(max_length=100, verbose_name='Codigo')),
                ('status', models.IntegerField(default='0', null=True, verbose_name='Status')),
                ('categoria', models.IntegerField(default='0', verbose_name='Categoria')),
            ],
            options={
                'db_table': 'equipos_equipos',
                'managed': False,
            },
        ),
    ]
