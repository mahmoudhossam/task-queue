from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery(
    "queue",
    broker="redis://redis:6379",
    backend="redis://redis:6379",
    imports=["tasks"],
)

if __name__ == "__main__":
    app.start()
