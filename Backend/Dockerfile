FROM python:3.10.7-alpine

WORKDIR /app

ADD . /app

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "--config", "conf/gunicorn_config.py", "products_api:app"]