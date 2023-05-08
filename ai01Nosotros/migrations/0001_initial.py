# Generated by Django 4.1.7 on 2023-04-24 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('Cargo', models.CharField(max_length=50)),
                ('FotoPerfil', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': '03Equipo',
                'verbose_name_plural': '03Equipos',
            },
        ),
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Periodo', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': '02Historia_Periodo',
                'verbose_name_plural': '02Historias_Periodos',
            },
        ),
        migrations.CreateModel(
            name='Valores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=50)),
                ('Contenido', models.TextField(max_length=5000)),
            ],
            options={
                'verbose_name': '01Valore',
                'verbose_name_plural': '01Valores',
            },
        ),
        migrations.CreateModel(
            name='ValoresFinal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=50)),
                ('Contenido', models.TextField(max_length=5000)),
            ],
            options={
                'verbose_name': '04Valore_Final',
                'verbose_name_plural': '04Valores_Finales',
            },
        ),
        migrations.CreateModel(
            name='Cronologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Agno', models.IntegerField()),
                ('Contenido', models.CharField(max_length=100)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ai01Nosotros.historia')),
            ],
            options={
                'verbose_name': '02Historia',
                'verbose_name_plural': '02Historias',
            },
        ),
    ]
