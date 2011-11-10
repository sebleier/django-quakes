=============
Django Quakes
=============


Django quakes is a simple app to download USGS data for recent earthquakes.

Comes with a model to store earthquake information and function to import it
from the USGS website.  The function in invoked by either management command
or by a celery periodic task.


Install
-------

To install you need to clone the repo and use the setup.py to install::

    python setup.py install

To run the periodic task, you need to have celery setup.  There is an example
project that uses a barebones django settings file for setting up the
django-quakes app with redis.

Management Command
------------------

To invoke from the management command::

    ./manage.py load_quakes


