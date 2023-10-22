FROM python:3.10 AS builder
ENV PYTHONUNBUFFERED 1

RUN python --version

WORKDIR /core

ADD ./core ./core
ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt
RUN pip install -e core/
