# Generated by Django 4.0.5 on 2023-06-15 11:51

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0005_alter_empleado_ci'),
        ('areadenegocio', '0002_remove_areadenegocio_paises_areadenegocio_pais_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areadenegocio',
            name='descripcion',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción del área de negocio'),
        ),
        migrations.AlterField(
            model_name='areadenegocio',
            name='id_empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='empresa_del_area_de_negocio', to='empresa.empresa', verbose_name='Empresa relacionada'),
        ),
        migrations.AlterField(
            model_name='areadenegocio',
            name='pais',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255, verbose_name='País'), blank=True, null=True, size=None),
        ),
    ]