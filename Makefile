APP = restapi

test:
	flake8 . --exclude .venv
	pytest -v --disable-warnings

compose:
	docker-compose down
	docker-compose build
	docker-compose up

container_build:
	docker run --env FLASK_ENV=development rest-api:0.2