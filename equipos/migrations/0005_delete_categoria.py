# Generated by Django 4.1.2 on 2022-10-14 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0004_categoria'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]