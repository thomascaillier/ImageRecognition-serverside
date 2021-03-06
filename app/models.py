import os

from django.db import models

import app


class Image(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    file = models.ImageField(
        upload_to='images/base',
        default=None,
        blank=True,
        null=False
    )


class CorrespondingImages(models.Model):
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


