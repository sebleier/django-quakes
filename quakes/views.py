import datetime
from datetime import timedelta
from django.conf import settings
from quakes.decorators import json, gzip
from quakes.models import Quake

@gzip
@json
def earthquakes(request):
    data = {}
    weekago = datetime.datetime.now() - datetime.timedelta(days=7)
    quakes = Quake.objects.filter(date__gte=weekago).order_by('date')
    bounds = getattr(settings, 'BOUNDS', None)
    if bounds is not None:
        quakes = quakes.filter(point__contained=bounds)
    for quake in quakes:
        if quake.date > datetime.datetime.now() - timedelta(hours=1):
            timeframe = "h"
        elif quake.date > datetime.datetime.now() - timedelta(days=1):
            timeframe = "d"
        else:
            timeframe = "w"
        if int(quake.magnitude) < 2:
            continue
        data[quake.eqid] = {
            'eqid': quake.eqid,
            'magnitude': quake.magnitude,
            'timeframe': timeframe,
            'lat': quake.point.coords[1],
            'lon': quake.point.coords[0],
        }
    return data
