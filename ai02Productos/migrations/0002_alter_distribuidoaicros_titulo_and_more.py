# Generated by Django 4.1.7 on 2023-04-27 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai02Productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribuidoaicros',
            name='Titulo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='productosaicros',
            name='Titulo',
            field=models.CharField(max_length=100),
        ),
    ]
