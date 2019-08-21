FROM python:3.7-buster
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8

RUN mkdir /code
WORKDIR /code

RUN pip install django psycopg2 && \
    apt-get update -qq && \
    apt-get upgrade -y -qq && \
    apt-get install -y -qq binutils libproj-dev gdal-bin libgdal-dev python3-gdal libgeos-3.7.1

COPY . /code/
