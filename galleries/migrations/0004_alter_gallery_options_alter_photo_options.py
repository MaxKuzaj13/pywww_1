# Generated by Django 4.0 on 2021-12-28 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0003_auto_20211208_1355'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Galeria', 'verbose_name_plural': 'Galerje'},
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'Zdjęcie', 'verbose_name_plural': 'Zdjęcia'},
        ),
    ]
