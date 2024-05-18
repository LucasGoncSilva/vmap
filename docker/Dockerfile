FROM python:latest

WORKDIR /code

COPY /VMAP/requirements.txt /code/

RUN pip install -r requirements.txt

COPY /VMAP /code/

RUN python manage.py collectstatic --no-input
