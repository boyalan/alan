from app import celery
from app.celery_flask.logic import do_send_email

@celery.task
def send_email(fromemail,toemail, subject,content):
    return do_send_email(fromemail,toemail, subject,content)
