
all: down build docker-makemigrations migrate up

migrate:
	docker-compose run --rm app python src/manage.py migrate $(if $m, api $m,)

makemigrations:
	python src/manage.py makemigrations
	sudo chown -R ${USER} src/app/migrations/

docker-makemigrations:
	docker-compose run --rm app python src/manage.py makemigrations

createsuperuser:
	docker-compose run --rm app python src/manage.py createsuperuser

collectstatic:
	docker-compose run --rm app python src/manage.py collectstatic --no-input

dev:
	docker-compose run --rm app python src/manage.py runserver localhost:8000

command:
	docker-compose run --rm app python src/manage.py ${c}

shell:
	docker-compose run --rm app python src/manage.py shell

debug:
	docker-compose run --rm app python src/manage.py debug

piplock:
	docker-compose run --rm app pipenv install && sudo chown -R ${USER} Pipfile.lock

lint:
#	isort .
#	flake8 --config setup.cfg
#	black --config pyproject.toml .
	echo "zdes' bil lint"

check_lint:
#	docker run --rm app
#	docker-compose run --rm app isort --check --diff .
#	docker-compose run --rm app flake8 --config setup.cfg
#	docker-compose run --rm app black --check --config pyproject.toml .
	echo "zdes' bil lint"


build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

pull:
	docker-compose pull ${IMAGE_APP}

push:
	docker-compose push ${IMAGE_APP}

test:
	echo "tests"
