FROM python:slim-buster

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir selenium
RUN pip install --no-cache-dir pymongo
RUN pip install --no-cache-dir bs4


CMD ["/bin/bash", "-c", "while true; do python3 ./faster_crawler.py && sleep 10800; done"]