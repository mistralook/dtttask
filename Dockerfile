FROM python:3.9-slim-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY Pipfile Pipfile.lock /app/

RUN apt update && \
    apt-get install -y netcat && \
    pip install --no-cache pipenv && \
    pipenv install

EXPOSE 8000

COPY . /app

#RUN chmod +x /app/entrypoint.sh
#ENTRYPOINT ["/bin/sh", "./entrypoint.sh"]