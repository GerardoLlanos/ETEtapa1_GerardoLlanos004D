# Generated by Django 3.2.3 on 2021-06-29 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_rename_pais_paises'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/colaborador/'),
        ),
    ]
