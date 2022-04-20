# syntax=docker/dockerfile:1
FROM python:3.9

ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/blablog

COPY requirements.txt .
COPY entrypoint.sh .

RUN pip install -r requirements.txt

COPY . .
ENTRYPOINT ["sh", "/usr/src/blablog/entrypoint.sh"]