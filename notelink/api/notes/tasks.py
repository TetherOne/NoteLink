from notelink.core.helpers import db_helper
from notelink.core.models import Note
from notelink.core.settings.celery import celery


@celery.task
def delete_note_at_expire_time(note_id):
    with db_helper.session_getter() as session:
        note = session.get(Note, note_id)
        if note:
            session.delete(note)
            session.commit()
