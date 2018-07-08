init:
	pip install --upgrade pipenv
	pipenv install

test:
	pipenv run pytest tests