APP = restapi

test:
	flake8 . --exclude .venv
compose:
	docker-compose down
	docker-compose build
	docker-compose up