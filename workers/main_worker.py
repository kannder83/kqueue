
import time
from celery import Celery
from config.conf import settings

celery = Celery("celery_worker")
celery.conf.broker_url = settings.celery_broker_url
celery.conf.result_backend = settings.celery_result_backend


@celery.task(name="create_task")
def create_task(a, b, c):
    time.sleep(a)
    result = b + c
    print(f"result: {result}")
    return result
