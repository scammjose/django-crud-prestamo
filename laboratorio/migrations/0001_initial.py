# Generated by Django 4.1.2 on 2022-10-28 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratorios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imagen', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('status', models.IntegerField(default='0', null=True, verbose_name='Status')),
            ],
        ),
    ]