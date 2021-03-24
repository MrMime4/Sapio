from django.db import models
from django.utils import timezone

# Create your models here.
class Records(models.Model):
    stamp = models.DateTimeField()
    direction = models.CharField(max_length=5)