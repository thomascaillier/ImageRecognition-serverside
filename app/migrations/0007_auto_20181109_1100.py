# Generated by Django 2.1.2 on 2018-11-09 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20181109_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='base_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/base'),
        ),
        migrations.AlterField(
            model_name='image',
            name='zone_detected_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/zone_detected'),
        ),
    ]
