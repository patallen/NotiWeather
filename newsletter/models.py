from django.db import models


class Location(models.Model):
    """
    Stores a city, its state's full length name, and it's state's two letter
    shortcode. This should be normalized to include a table solely for state,
    but we will leave it as is to keep it simple for this project.
    """
    city = models.CharField(max_length=100)
    state_long = models.CharField(max_length=100)
    state_short = models.CharField(max_length=2)


class User(models.Model):
    """
    Stores the user's email and the city that they reside in. The email field
    must be unique throughout the table. The location is a foreign key
    relationship to the Location model.
    """
    email = models.EmailField(blank=False, unique=True)
    location = models.ForeignKey(Location, blank=False)
