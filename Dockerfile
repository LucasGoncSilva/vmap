FROM python:latest

WORKDIR /code

COPY ${PROJECT_NAME}/requirements.txt /code/

RUN pip install -r requirements.txt

COPY /${PROJECT_NAME} /code/
