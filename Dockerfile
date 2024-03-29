FROM python:3.7-buster
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV TNS_ADMIN /code/apb_oracle_tns_admin

RUN mkdir /code
WORKDIR /code
COPY requirements_pip.txt requirements_pip.txt

RUN apt-get update -qq && \
    apt-get install -y -qq apt-utils binutils postgresql-client && \
    apt-get install -y -qq libproj-dev gdal-bin libgdal-dev python3-gdal libgeos-3.7.1 libsqlite3-mod-spatialite && \
    pip install --requirement requirements_pip.txt

RUN apt-get install -y -qq libaio-dev alien

ADD oracle-instantclient*.rpm /tmp/

RUN alien /tmp/oracle-instantclient*.rpm

RUN dpkg -i oracle-instantclient*.deb

RUN rm -f /tmp/oracle-instantclient*.rpm && rm -f oracle-instantclient*.deb

#RUN apt-get install -y /tmp/oracle-instantclient*.rpm && \
#     rm -rf /var/cache/yum && \
#     rm -f /tmp/oracle-instantclient*.rpm && \
RUN echo /usr/lib/oracle/12.2/client64/lib > /etc/ld.so.conf.d/oracle-instantclient12.2.conf && \
     ldconfig

ENV PATH=$PATH:/usr/lib/oracle/12.2/client64/bin