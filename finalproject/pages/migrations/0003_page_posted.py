# Generated by Django 3.2.4 on 2021-06-08 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_page_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='posted',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha de carga de la imagen'),
        ),
    ]
