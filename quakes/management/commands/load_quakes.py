import urllib2
from django.core.management.base import NoArgsCommand
from django.contrib.gis.geos import Point
from quakes.models import Quake
from dateutil.parser import parse
from csv import DictReader


def load_quake_data():
    url = "http://earthquake.usgs.gov/eqcenter/catalogs/eqs7day-M1.txt"
    resource = urllib2.urlopen(url)
    reader = DictReader(resource)
    new_quakes = []

    for quake in reader:
        # Transform the keys to lowercase
        quake = dict((key.lower(), value) for key, value in quake.items())

        # Pop the lon and lat and add them
        quake['point'] = Point(float(quake.pop('lon')), float(quake.pop('lat')))

        # Parse the datetime
        quake['datetime'] = parse(quake['datetime'])

        # Get or create the Quake and count if it is created
        quake, created = Quake.objects.get_or_create(eqid=quake['eqid'], defaults=quake)
        if created:
            new_quakes.append(quake)

    return new_quakes


class Command(NoArgsCommand):
    help = "Scrapes the USGS earthquake feed"

    def handle(self, **options):
        load_quake_data()

