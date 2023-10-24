.PHONY: all
run:
	poetry run python src/main.py 
build:
	docker-compose up --build
delete:
	docker system prune -a -f --filter "until=24h"
	docker system prune --volumes -f

lint:
	poetry run pflake8 src
	poetry run isort --check --diff src
	poetry run black --check src
	poetry run mypy src

format:
	poetry run isort src
	poetry run black src

