FROM python:3
ENV PYTHONUNBUFFERED 1
ENV http_proxy 'http://10.10.16.8:3128'
ENV https_proxy 'http://10.10.16.8:3128'
ENV PIP_OPTIONS="--proxy $HTTP_PROXY"
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install --proxy 'http://10.10.16.8:3128' -r requirements.txt