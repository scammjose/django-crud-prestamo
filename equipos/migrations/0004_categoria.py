# Generated by Django 4.1.2 on 2022-10-14 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0003_alter_equipos_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(max_length=100, verbose_name='Categoria')),
            ],
        ),
    ]
