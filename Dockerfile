FROM python:3.10 AS builder
ENV PYTHONUNBUFFERED 1
#RUN apt-get update && apt-get install -y python3.10

RUN python --version

WORKDIR /core_dir

ADD ./core ./core
ADD requirements.txt requirements.txt

RUN pip install -U pip
RUN pip install -r requirements.txt
CMD ["python"]