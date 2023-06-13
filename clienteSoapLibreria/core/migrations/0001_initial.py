# Generated by Django 4.0.4 on 2023-06-13 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('idServicio', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de servicio')),
                ('nombreServicio', models.CharField(max_length=50, verbose_name='Nombre de la servicio')),
                ('descripcion', models.CharField(max_length=50, verbose_name='descripcion')),
            ],
        ),
    ]
