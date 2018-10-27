# coding=utf-8
"""
celery worker -A celery_app.celery --loglevel=info
"""

import os
import sys
import time
from celery import Celery

curr_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, curr_dir)

# 加载.env环境变量
from flask.cli import load_dotenv
load_dotenv()

celery_conf = {
    'CELERY_BROKER_URL': os.getenv('CELERY_BROKER_URL') or 'amqp://guest:guest@localhost:5672//',  # nopep8
    'CELERY_RESULT_BACKEND': os.getenv('CELERY_RESULT_BACKEND') or 'amqp://guest:guest@localhost:5672//'  # nopep8
}
celery = Celery('celery_app', broker='amqp://guest:guest@localhost:5672//')
celery.conf.update(celery_conf)


@celery.task
def background_task():
    # 最好在函数里导入flask app，放在外面可能会导致socketio失效
    from flask_app import socketio, namespace
    socketio.emit(
        'data', {'data': 'Task starting...'},
        namespace=namespace
    )
    time.sleep(3)
    socketio.emit(
        'data', {'data': 'Task complete!'},
        namespace=namespace
    )


@celery.task
def async_task():
    print('Async!')
    time.sleep(5)
