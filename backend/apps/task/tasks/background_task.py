# coding=utf-8

import time
from ..celery_app import celery
from ..send_message import send_message


@celery.task
def background_task():
    # 最好在函数里导入flask app，放在外面可能会导致socketio失效
    # from apps.web.flask_app import socketio, namespace
    send_message({'data': 'Task starting...'})
    time.sleep(3)
    send_message({'data': 'Task complete!'})
