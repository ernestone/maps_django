FROM python:3.7-buster
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8

RUN mkdir /code
WORKDIR /code
COPY requirements_pip.txt requirements_pip.txt

RUN apt-get update -qq && \
    apt-get install -y -qq apt-utils binutils postgresql-client && \
    apt-get install -y -qq libproj-dev gdal-bin libgdal-dev python3-gdal libgeos-3.7.1 libsqlite3-mod-spatialite && \
    pip install --requirement requirements_pip.txt
