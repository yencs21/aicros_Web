# Generated by Django 4.1.7 on 2023-04-25 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Servicio', models.CharField(max_length=500)),
                ('Iconos', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': '01Servicio',
                'verbose_name_plural': '01Servicios',
            },
        ),
    ]