# Generated by Django 3.1.4 on 2020-12-06 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asistencia',
            old_name='al',
            new_name='alumno',
        ),
        migrations.RenameField(
            model_name='materia',
            old_name='yr',
            new_name='year',
        ),
    ]