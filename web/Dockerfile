FROM python:3
RUN mkdir /django
WORKDIR /django
COPY req.txt /django/
RUN pip install -r req.txt
COPY . /django/