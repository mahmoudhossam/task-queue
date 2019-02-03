FROM python:3.7-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "publisher.py"]
