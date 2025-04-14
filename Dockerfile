FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

RUN apt-get update

WORKDIR /app

COPY ./requirements/ /app/requirements/

RUN pip install --upgrade pip setuptools wheel && \
    pip install -r /app/requirements/requirements.txt --root-user-action=ignore

ENV PYTHONBREAKPOINT=ipdb.set_trace

COPY . /app/

STOPSIGNAL SIGINT

COPY entrypoint.sh /

ENTRYPOINT [ "/entrypoint.sh" ]