# coding=utf-8
import time
from apps.task.celery_app import celery


@celery.task
def async_task():
    print('Async!')
    time.sleep(5)
