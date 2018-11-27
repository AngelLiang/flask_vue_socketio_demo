# coding=utf-8

from apps.web.flask_app import app
from apps.web.flask_app import socketio

if __name__ == '__main__':
    socketio.run(app, debug=True)
