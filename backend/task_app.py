"""
celery worker -A task_app.celery --loglevel=info
"""

from apps.task.celery_app import celery
