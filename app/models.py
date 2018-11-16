from django.db import models
from jsonfield import JSONField


class Image(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    base_image = models.ImageField(
        upload_to='images/base',
        default=None,
        blank=True,
        null=True
    )
    zone_detected_image = models.ImageField(
        upload_to='images/zone_detected',
        default=None,
        blank=True,
        null=True
    )
    corresponding_data = JSONField(
        default={}
    )
