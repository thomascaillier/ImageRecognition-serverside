# Generated by Django 2.1.2 on 2019-04-08 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190408_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='base_image',
            field=models.ImageField(blank=True, default=None, upload_to='C:\\Users\\thoma\\source\\ImageRecognition-serverside\\app/images/base'),
        ),
    ]
