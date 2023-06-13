# Generated by Django 4.0.5 on 2023-04-22 02:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0003_alter_empresa_cliente_empresa_alter_empresa_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='logo',
            field=models.FileField(default='logo.png', upload_to='images/logos'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='ci',
            field=models.TextField(validators=[django.core.validators.RegexValidator(code='ci_invalido', message='El campo debe ser una cédula de identidad o número de pasaporte', regex='^(([a-zA-Z]-)[0-9]{1,3}\\.?[0-9]{1,3}\\.?[0-9]{1,3})$|^([0-9A-Z]{10})$')], verbose_name='Cédula o nro pasaporte'),
        ),
    ]
