from django.db import models

from tires.models import Tires


class Car(models.Model):
    name = models.CharField('모델', max_length=40)
    year = models.IntegerField('출시년도', default=2018)
    color = models.CharField('색상', max_length=20, default='white')
    tires = models.ForeignKey(Tires)
