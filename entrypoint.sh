#!bin/sh

echo "Waiting for database..."

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  echo "Database in not ready yet" $(date)
  sleep 2
done

echo "Database started"


