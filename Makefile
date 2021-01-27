

run: 
	python -m boardgame.main

format:
	@isort  boardgame
	python -m black boardgame

test:
	python -m pytest --cov=boardgame

test-cov:
	python -m pytest --cov=boardgame --cov-report html