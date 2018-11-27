# coding=utf-8
# flake8: noqa
"""
celery worker -A apps.task.celery --loglevel=info
"""

import os
import sys
import time
from celery import Celery

BASEDIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))))
sys.path.insert(0, BASEDIR)

# 加载.env环境变量
# from flask.cli import load_dotenv
# load_dotenv()

from apps.web.flask_app import socketio, namespace

celery_conf = {
    'CELERY_BROKER_URL': os.getenv('CELERY_BROKER_URL') or 'amqp://guest:guest@127.0.0.1:5672//',
    'CELERY_RESULT_BACKEND': os.getenv('CELERY_RESULT_BACKEND') or 'amqp://guest:guest@127.0.0.1:5672//'
}
celery = Celery(__name__, broker='amqp://guest:guest@localhost:5672//')
celery.conf.update(celery_conf)

# 这种方式导入不成功
# from apps.task.tasks.background_task import background_task
# from apps.task.tasks.async_task import async_task

from apps.task.background_task import background_task

# 只能使用下面的方式
# 与 celery app 平级
from .send_message import send_message

# 或者直接放在这里
# @celery.task
# def background_task():
#     # 最好在函数里导入flask app，放在外面可能会导致socketio失效
#     # from apps.web.flask_app import socketio, namespace
#     send_message({'data': 'Task starting...'})
#     time.sleep(3)
#     send_message({'data': 'Task complete!'})


@celery.task
def async_task():
    print('Async!')
    time.sleep(5)
