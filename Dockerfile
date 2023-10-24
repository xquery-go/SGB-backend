FROM python:3.10-slim-bullseye AS builder
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && pip install --no-cache-dir --upgrade pip

WORKDIR /application

COPY ./requirements.txt ../application

RUN pip install -r requirements.txt

COPY . /application

RUN pip install -e core/
