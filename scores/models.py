from __future__ import unicode_literals

from django.db import models

# Create your models here.
class College(models.Model):
    college_name = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    SAT25pScore = models.IntegerField(default=0)
    SAT75pScore = models.IntegerField(default=0)
