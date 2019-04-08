# Generated by Django 2.1.2 on 2019-04-07 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='corresponding_data',
        ),
        migrations.RemoveField(
            model_name='image',
            name='zone_detected_image',
        ),
        migrations.AlterField(
            model_name='image',
            name='base_image',
            field=models.ImageField(blank=True, default=None, upload_to='images/base'),
        ),
    ]