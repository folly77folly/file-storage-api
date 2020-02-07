# FROM directive instructing base image to build upon
FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY . .

RUN pip install -r requirements.txt

# CMD python manage.py runserver 0.0.0.0:$PORT
CMD gunicorn config.wsgi:application