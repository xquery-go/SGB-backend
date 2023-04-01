FROM python:3.10 AS builder

RUN apt-get update && apt-get install -y python3.10

RUN python --version

WORKDIR aaa_codebase/

ADD core/ ./core
ADD requirements.txt requirements.txt

RUN pip install -U pip
RUN pip install --prefix=/install -r requirements.txt

FROM python:3.10

WORKDIR /app

COPY --from=builder /install /usr/local

ADD core/ ./core

CMD ["python"]


