# flask_vue_socketio_demo

Flask和Vue使用SocketIO示例，并使用Celery异步任务队列通过SocketIO通知前端。

## 本人测试时的环境和主要工具版本

- Windows 10
- Python 3.6.6
    - Flask 1.0.2
    - Flask-SocketIO 3.0.2
    - celery 3.1.25（Windows下不支持Celery4）
- NodeJS
    - npm 5.6.0
    - node 8.9.3
    - vue 2.5.2
    - vue-socket.io 2.1.1-b
- RabbitMQ：用于Celery和Flask-SocketIO

## 步骤

### 依赖

除了Python和NodeJS，还需要RabbitMQ或Redis，如果没有可试试`flask_app_without_mq.py`。不过执行celery task时没法通过SocketIO向前端发送数据。

### 下载

```PowerShell
git clone git@github.com:AngelLiang/flask_vue_socketio_demo.git
```

### 启动后端

```PowerShell
# 后端
cd flask_vue_socketio_demo\backend
pipenv install
pipenv shell

# Console 1：启动Flask
python flask_app.py
# OR
python flask_app_without_mq.py

# Console 2：启动Celery
celery worker -A celery_app.celery --loglevel=info
```

### 启动前端

```PowerShell
# 前端
cd flask_vue_socketio_demo\frontend
npm install
npm run dev
```

然后访问 http://127.0.0.1:8080/ 即可。

## 效果图

![demo](/screenshot/demo.png)
