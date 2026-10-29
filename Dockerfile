FROM python:3.15-bookworm

LABEL maintainer="Amir Mallaei <amirmallaei@gmail.com>"

ENV PYTHONUNBUFFERED=1

RUN apt-get update -y 
RUN pip install --upgrade pip

RUN mkdir /code

ADD requirements.txt /code

WORKDIR /code

RUN pip install -r requirements.txt


ADD ./code /code

RUN useradd --create-home mobin \
    && chown -R mobin:mobin /code

USER mobin