from django.core.management.base import BaseCommand
from newsletter.models import Location

import csv
import os

directory = os.path.dirname(os.path.realpath(__file__))
csv_path = directory +  '/topcities.csv'

class Command(BaseCommand):
    """
    Custom Django manage.py command that seeds the database with the top 100
    cities by population.

    Usage: `$ python manage.py seed`
    """
    def handle(self, *args, **options):
        with open(csv_path, 'r') as csvfile:
            cityreader = csv.reader(csvfile, delimiter=',')
            for city in cityreader:
                try:
                    Location.objects.get_or_create(city=city[0],
                                                   state_long=city[1],
                                                   state_short=city[2])
                except:
                    pass