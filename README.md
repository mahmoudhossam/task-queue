Task-queue
=============

## Description
Process CSV files and send them to a message queue where the records are then saved in a database.

## Usage
To run this project, simply run `docker-compose up`.

## Libraries used

* celery
* redis-py
* psycopg2
* sqlalchemy
* sqlalchemy-utils

## Rationale

In `processor.py` you'll find the logic to parse the CSV file and run the tasks backed by the message queue (I used redis).

`db.py` contains all the database related code, while `tasks.py` contains a simple celery task that uses this code to run the database insertions asynchronously on the workers.

The whole project runs inside docker to simplify operation, all that is needed is the command above to run the project.

To handle the duplicate emails, I chose to update the username each time an existing email is encountered but of course this will change based on the business requirement.

To check that records have been inserted correctly in the database, use the command:

`docker-compose exec postgres psql -U user users -c "SELECT * FROM users ORDER BY id;"`

## What could've been done differently

* I'd have done upserts more efficiently since postgres supports them.
* Wrote tests.
* Built an API around this in flask or similar.
* Run a CI server for those tests to run on every pull request to this project.
* Deployed this to a real life server (or used something like kubernetes if it's a large project).
