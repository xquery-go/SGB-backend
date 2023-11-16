FROM python:3.10 AS build
ENV PYTHONUNBUFFERED 1

WORKDIR /application

ADD ./requirements.txt ../application

RUN pip install -r requirements.txt

ADD ./core ./core

RUN pip install core/
