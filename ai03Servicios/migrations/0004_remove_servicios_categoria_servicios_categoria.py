# Generated by Django 4.1.7 on 2023-04-28 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aicrosWeb', '0003_alter_a1promociones_contenido_and_more'),
        ('ai03Servicios', '0003_servicios_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicios',
            name='Categoria',
        ),
        migrations.AddField(
            model_name='servicios',
            name='Categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='aicrosWeb.a4negocio'),
            preserve_default=False,
        ),
    ]
