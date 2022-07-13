FROM python:3.9.13-alpine3.16

RUN mkdir /app
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
