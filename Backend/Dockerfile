FROM python:slim-buster

WORKDIR /app

ADD . /app

RUN pip install --upgrade pip
RUN python3 -m pip install flask
RUN python3 -m pip install pymongo
RUN python3 -m pip install flask_cors
RUN python3 -m pip install flask_redis
RUN python3 -m pip install flask_restful
RUN python3 -m pip install gunicorn
RUN python3 -m pip install selenium
RUN python3 -m pip install bs4

EXPOSE 8000

CMD ["gunicorn", "--config", "./conf/gunicorn_conf.py", "products_api:app"]