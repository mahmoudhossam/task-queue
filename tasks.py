from celery_app import app
from db import DB, User


@app.task
def task(message):
    """This handles adding the user to the database."""
    db = DB()
    user = User(name=message["name"], email=message["email"])
    db.add(user)
