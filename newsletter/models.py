from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=100)
    state_long = models.CharField(max_length=100)
    state_short = models.CharField(max_length=2)

class User(models.Model):
    email = models.EmailField(blank=False, unique=True)
    location = models.ForeignKey(Location, blank=False)