from celery import Celery
from decouple import config

celery = Celery(backend=config("CELERY_RESULT_BACKEND"),
                broker=config("CELERY_BROKER_URL"))


@celery.task
def notify():
    # TODO: send_email_to_cfo
    pass
