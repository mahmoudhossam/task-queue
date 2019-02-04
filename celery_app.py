from __future__ import absolute_import, unicode_literals
from celery import Celery
import os

broker_url = os.getenv("BROKER_URL")

app = Celery("queue", broker=broker_url, backend=broker_url, imports=["tasks"])

if __name__ == "__main__":
    app.start()
