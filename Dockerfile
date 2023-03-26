FROM python

RUN apt-get update && apt-get install -y python3.10

RUN python --version

WORKDIR aaa_codebase/

ADD core/ ./core
ADD requirements.txt requirements.txt

RUN pip install -U pip
RUN pip install -r requirements.txt




