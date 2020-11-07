From python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR  /app

ADD . /app
COPY ./requirements.txt /app/requirements.txt

COPY . /app