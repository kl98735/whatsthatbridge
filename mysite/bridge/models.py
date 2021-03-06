from django.db import models


class Bridge(models.Model):
    name = models.CharField(max_length=600)
    description = models.CharField(max_length=600, default="this bridge has no description")
    year_built = models.CharField(max_length=600, default="this bridge has no information on year built")
    lat = models.CharField(max_length= 100, default="0")
    long = models.CharField(max_length=100, default= "0")
