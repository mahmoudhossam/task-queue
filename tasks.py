from celery_app import app
from db import session, User


@app.task
def task(message):
    user = User(name=message["name"], email=message["email"])
    session.add(user)
    session.commit()
