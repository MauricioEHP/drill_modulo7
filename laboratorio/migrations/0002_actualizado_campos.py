# Generated by Django 4.1.1 on 2023-08-10 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='directorgeneral',
            name='especialidad',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='lab_ciudad',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='lab_pais',
            field=models.CharField(max_length=30, null=True),
        ),
    ]