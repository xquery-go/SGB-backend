FROM python:3.10 AS build
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y nano

WORKDIR /application

ADD ./requirements.txt ../application

RUN pip install -r requirements.txt

ADD ./core ./core

RUN pip install core/
