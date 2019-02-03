FROM python:3.7-alpine

RUN apk add --no-cache git postgresql-dev build-base

WORKDIR /app

RUN adduser -S -D -g '' queue

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

USER queue

ENTRYPOINT ["/app/entrypoint.sh"]

CMD ["python", "processor.py"]
