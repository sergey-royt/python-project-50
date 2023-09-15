lint:
	poetry run flake8 gendiff
test:
	poetry run pytest -vv
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
