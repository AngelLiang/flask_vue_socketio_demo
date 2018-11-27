# coding=utf-8
"""
Require:
    Redis OR RabbitMQ

Install:
    pipenv install flask flask_socketio celery==3.1.25

Run:
    celery worker -A celery_app.celery --loglevel=info
    python flask_app.py
"""

from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
CORS(app)

# 使用 RabbitMQ 存储 SocketIO 的消息队列，
# 否则celery的task调用socketio不成功
socketio = SocketIO(message_queue='amqp://guest:guest@localhost:5672//',
                    async_mode='threading')
socketio.init_app(app)
namespace = '/message'


@socketio.on('data', namespace=namespace)
def handle_data_with_namespace(message):
    print('message: ' + str(message))
    socketio.emit('data', message, namespace=namespace)


@app.route('/task', methods=['GET', 'POST'])
def start_background_task():
    from apps.task.celery_app import background_task
    background_task.delay()
    return 'Started'


@app.route('/send', methods=['GET', 'POST'])
def send():
    socketio.emit(
        'data', {'data': 'Hello!'},
        namespace=namespace
    )
    return 'Success'


if __name__ == '__main__':
    socketio.run(app, debug=True)
