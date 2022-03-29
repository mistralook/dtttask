
all: down build makemigrations migrate up

migrate:
	docker-compose exec app python src/manage.py migrate $(if $m, api $m,)

makemigrations:
	python src/manage.py makemigrations
	sudo chown -R ${USER} src/app/migrations/

createsuperuser:
	docker-compose exec app python src/manage.py createsuperuser

collectstatic:
	docker-compose exec app python src/manage.py collectstatic --no-input

dev:
	docker-compose exec app python src/manage.py runserver localhost:8000

command:
	docker-compose exec app python src/manage.py ${c}

shell:
	docker-compose exec app python src/manage.py shell

debug:
	docker-compose exec app python src/manage.py debug

piplock:
	pipenv install
	sudo chown -R ${USER} Pipfile.lock

lint:
	isort .
	flake8 --config setup.cfg
	black --config pyproject.toml .

check_lint:
	docker-compose run app isort --check --diff .
	docker-compose run app flake8 --config setup.cfg
	docker-compose run app black --check --config pyproject.toml .

build:
	docker-compose up --build

up:
	docker-compose up

down:
	docker-compose down
