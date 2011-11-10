=============
Django Quakes
=============


Django quakes is a simple app to download and display USGS data on recent
earthquake data.

Comes with a model to store earthquake information and function to import it
from the USGS website.  The function in invoked by either management command
or by a celery periodic task.

Management Command
------------------

To invoke from the management command::

    ./manage.py load_quakes


