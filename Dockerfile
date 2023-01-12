# syntax=docker/dockerfile:1

FROM python:slim-buster

WORKDIR /app

COPY requirements.txt /app

RUN ["pip", "install", "-r", "requirements.txt"]

COPY ./better-call-reward.py /app

CMD [ "python3", "-u", "better-call-reward.py"]
