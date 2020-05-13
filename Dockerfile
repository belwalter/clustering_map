FROM python:latest

WORKDIR /api
COPY api/ .

RUN pip3 install flask pymongo 

EXPOSE 5000