from django.db import models


class Tires(models.Model):
    name = models.CharField('브랜드명', max_length=40)
    size = models.FloatField('사이즈', default=17.0)


class Car(models.Model):
    name = models.CharField('모델', max_length=40)
    year = models.IntegerField('출시년도', default=2018)
    color = models.CharField('색상', max_length=20, default='white')
    tires = models.ForeignKey(Tires)
