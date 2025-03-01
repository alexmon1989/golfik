FROM python:3.6-alpine
ENV PYTHONUNBUFFERED=1
RUN apk add --no-cache \
    postgresql-dev gcc python3-dev musl-dev libffi-dev \
    jpeg-dev zlib-dev
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
