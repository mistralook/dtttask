FROM python:3.9-slim-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt update && \
    apt-get install -y netcat && \
    pip install --no-cache pipenv && \
    rm -rf /var/lib/apt/lists/*

COPY Pipfile Pipfile.lock /app/

RUN pipenv install --system

EXPOSE 8000

COPY . /app

#RUN chmod +x /app/entrypoint.sh
#ENTRYPOINT ["/bin/sh", "./entrypoint.sh"]