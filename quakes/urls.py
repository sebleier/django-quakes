from django.conf.urls.defaults import *
from quakes.views import earthquakes


urlpatterns = patterns('',
    (r'^json/$', earthquakes),
)

