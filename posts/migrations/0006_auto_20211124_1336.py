# Generated by Django 3.2.5 on 2021-11-24 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20211119_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='example_field',
            field=models.FileField(blank=True, null=True, upload_to='post/examples'),
        ),
        migrations.AddField(
            model_name='post',
            name='image_field',
            field=models.ImageField(blank=True, null=True, upload_to='post/images/%Y/%m/%d/', width_field='image_width'),
        ),
        migrations.AddField(
            model_name='post',
            name='image_width',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]
