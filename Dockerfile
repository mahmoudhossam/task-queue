FROM python:3.7-alpine

RUN apk add --no-cache git postgresql-dev build-base

WORKDIR /app

RUN adduser -S -D -g '' queue

COPY requirements.txt .

RUN pip install -r requirements.txt

USER queue

CMD ["python", "processor.py"]
