FROM python:3.12

RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-rus \
    libtesseract-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY docker/*.sh /app/docker/
#RUN chmod a+x docker/*.sh   # разрешение запускать bash скрипты