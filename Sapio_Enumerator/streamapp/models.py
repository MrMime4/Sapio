from django.db import models
from django.utils import timezone

# Create your models here.
class Records(models.Model):
<<<<<<< HEAD
    stamp = models.TimeField()
<<<<<<<< HEAD:Sapio_Enumerator/streamapp/models.py
    direction = models.CharField(max_length=5)
    
========
    direction = models.CharField(max_length=5)
>>>>>>>> b5c60cd24ebed6da9eb4490924ee053df955720c:stream/streamapp/models.py
=======
    stamp = models.DateTimeField()
    direction = models.CharField(max_length=5)
    
>>>>>>> b5c60cd24ebed6da9eb4490924ee053df955720c
