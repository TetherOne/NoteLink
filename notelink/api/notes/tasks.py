from notelink.core.settings.celery import celery


@celery.task
def say_hello():
    pass
