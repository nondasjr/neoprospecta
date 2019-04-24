FROM python:3.7
MAINTAINER NondasJr <nondasjuniorsk8@gmail.com>

ENV PYTHONBUFFERED 1

RUN mkdir /code

WORKDIR /code
ADD requirements.txt /code/

RUN pip install -r requirements.txt

ADD . /code/