clean:
	find . -type d -name __pycache__ -exec rm -r {} \+

migrate: clean
	flask db migrate

upgrade: clean
	flask db upgrade
