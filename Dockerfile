FROM python:3.11.0-alpine

WORKDIR /usr/src/app

# prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# ensure Python output is sent directly to the terminal without buffering
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
# Install GTK and its dependencies
RUN apk add --no-cache gtk+3.0

COPY . /usr/src/app/
RUN python manage.py migrate 
