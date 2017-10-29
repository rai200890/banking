clean:
	find . -type d -name __pycache__ -exec rm -r {} \+

migrate: clean
	docker-compose exec web flask db migrate

upgrade: clean
	docker-compose exec web flask db upgrade

test: clean
	docker-compose exec web python -m pytest

flake8: clean
	docker-compose exec web python -m flake8

ci: test flake8
