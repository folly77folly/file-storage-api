# FROM directive instructing base image to build upon
FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY . .
RUN ls
RUN pip install -r requirements.txt

RUN ls
EXPOSE 8000
# CMD python manage.py runserver 0.0.0.0:8000