from django.contrib.gis.db import models


class Quake(models.Model):
    src = models.CharField(max_length=2)
    eqid = models.CharField(max_length=255, primary_key=True)
    version = models.CharField(max_length=2)
    datetime = models.DateTimeField()
    point = models.PointField(srid=4326)
    magnitude = models.FloatField()
    depth = models.FloatField()
    nst = models.IntegerField()
    region = models.CharField(max_length=255)

    objects = models.GeoManager()

    def __unicode__(self):
        return "%s in %s on %s" % (self.magnitude, self.region, self.datetime)
