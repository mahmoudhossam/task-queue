from celery_app import app
from db import DB, User

db = DB()


@app.task
def task(message):
    user = User(name=message["name"], email=message["email"])
    db.session.add(user)
    db.session.commit()
