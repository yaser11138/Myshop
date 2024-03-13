FROM python:3.10-alpine

WORKDIR /usr/src/app

# prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# ensure Python output is sent directly to the terminal without buffering
ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk add --no-cache gcc musl-dev libffi-dev openssl-dev
# Install weasyprint and its dependencies
RUN apk add weasyprint

# Install required packages for fonts
RUN apk add --no-cache fontconfig glib

# Copy font files to appropriate directory
COPY static/fonts /usr/share/fonts

# Install the font
RUN fc-cache -f -v

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt


COPY . /usr/src/app/
RUN python manage.py migrate 

