from django.db import models


class Image(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    base_image = models.ImageField(
        upload_to='images/base',
        default=None,
        blank=True,
        null=False
    )


class CorrespondingImages:
    id = models.AutoField(
        primary_key=True
    )
    image = models.ImageField(
        upload_to='corresponding_images',
        default=None,
        blank=True,
        null=False
    )
    base_image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE
    )
    score = models.FloatField(
        default=0,
        null=False
    )
