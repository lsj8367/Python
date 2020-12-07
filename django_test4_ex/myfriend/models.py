from django.db import models

# Create your models here.
class Friend(models.Model):
    irum = models.CharField(max_length = 20)
    juso = models.CharField(max_length = 100)
    nai = models.IntegerField()