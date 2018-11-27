# coding=utf-8

from apps.web.flask_app import socketio, namespace


def send_message(data):
    socketio.emit('data', data, namespace=namespace)
