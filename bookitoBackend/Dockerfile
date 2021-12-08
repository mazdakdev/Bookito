FROM python:3.7-alpine

RUN mkdir /backend
COPY . /backend
WORKDIR /backend
 
RUN pip install --upgrade pip

# Installing dependencies for building 
RUN apk update \
    && apk add  gcc python3-dev musl-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && apk add jpeg-dev zlib-dev libjpeg 

RUN apk add libc-dev make git libffi-dev openssl-dev  libxml2-dev libxslt-dev 
 

COPY ./requirements.txt /backend/

RUN pip install -r requirements.txt

COPY ./entrypoint.sh /

ENTRYPOINT [ "sh"  , "/entrypoint.sh"]

  