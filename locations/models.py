from django.db import models
from geolocation_fields.models import fields

# Create your models here.

class PointModel(models.Model):
    point = fields.PointField(verbose_name='Point')
