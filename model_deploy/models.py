from django.db import models

# Create your models here.


class Features(models.Model):
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    exp = models.CharField(max_length=100)
    educ_lvl = models.CharField(max_length=100)
    job = models.CharField(max_length=100)