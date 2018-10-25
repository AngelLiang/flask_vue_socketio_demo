# coding=utf-8
"""
Install:
    pipenv install flask flask_socketio celery==3.1.25

Run:
    python flask_app_without_mq.py
"""

from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
CORS(app)

socketio = SocketIO()
socketio.init_app(app)
namespace = '/message'


@socketio.on('data', namespace=namespace)
def handle_data_with_namespace(message):
    print('message: ' + str(message))
    socketio.emit('data', message, namespace=namespace)


@app.route('/task', methods=['GET', 'POST'])
def async_():
    from celery_app import background_task
    background_task.delay()
    socketio.emit(
        'data', {'data': "Task cann't send message!"},
        namespace=namespace
    )
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
