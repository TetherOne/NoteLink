from notelink.api.notes.celery import celery


@celery.task
def hello_world():
    pass
