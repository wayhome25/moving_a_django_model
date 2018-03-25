from django.db import models

# Create your models here.
class Tires(models.Model):
    name = models.CharField('브랜드명', max_length=40)
    size = models.FloatField('사이즈', default=17.0)
