from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class College(models.Model):
    college_name = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    SAT25pScore = models.IntegerField(default=0)
    SAT75pScore = models.IntegerField(default=0)

    def __str__(self):
        return self.college_name

    @property
    def serialize(self):
        return {
            'college_name': self.college_name,
            'region': self.region,
            'SAT25pScore': self.SAT25pScore,
            'SAT75pScore': self.SAT75pScore
        }
