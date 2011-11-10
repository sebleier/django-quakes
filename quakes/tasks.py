from celery.decorators import periodic_task
from celery.task.schedules import crontab
from quakes.management.commands.load_quakes import load_quake_data


@periodic_task(run_every=crontab(minute="*/10"))
def load_quakes():
    created = load_quake_data()
    logger = load_quakes.get_logger()
    logger.info("Adding %s new quakes" % len(created))
