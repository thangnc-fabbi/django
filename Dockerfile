FROM python:3.7.3-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code/
WORKDIR /code/

RUN apk add --update --no-cache \
        python3-dev \
        libstdc++ \
        jpeg-dev \
        zlib-dev \
        freetype-dev \
        lcms2-dev \
        openjpeg-dev \
        tiff-dev \
        tk-dev \
        tcl-dev \
        harfbuzz-dev \
        g++ \
        mariadb-dev \
        fribidi-dev \
        curl

RUN apk update && apk add --no-cache \
        msttcorefonts-installer \
        fontconfig \
        libx11 \
        libxml2 \
        libxml2-dev \
        libxslt-dev \
        libxrender \
        libxext \
        ca-certificates \
        && update-ms-fonts \
        && fc-cache -f

RUN apk update && apk add gcc python3-dev musl-dev

ADD requirements.txt /code/
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

ADD . /code/