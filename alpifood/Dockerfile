FROM python:3.6.9

ENV PYTHONUNBUFFERED 1

RUN mkdir /alpifood
WORKDIR /alpifood
ADD . /alpifood/
RUN pip install -r requirements.txt 