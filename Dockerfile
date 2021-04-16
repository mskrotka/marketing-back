FROM python:3.8-slim-buster

EXPOSE 8000

ENV PYTHONUNBUFFERED=1 \
    PORT=8000

ENV DJANGO_KEY=d55b&3zs6t&urj0l8j*o2+tjhw#(ne$m&@+ll=ebpnxrt=c&8s

WORKDIR /app

ADD . .

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --skip-lock --system --dev
