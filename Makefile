
help:                                                                                                                    
	@grep '^.PHONY: .* #' Makefile | sed 's/\.PHONY: \(.*\) # \(.*\)/\1 \2/' | expand -t20

.PHONY: clean # 	Delete .pyc .swp ad __pycache__ 
clean:
	@rm -f .coverage 2> /dev/null
	@rm -rf .cache 2> /dev/null
	@find . -name "*.pyc" -delete
	@find . -name "*.swp" -delete
	@find . -name "__pycache__" -delete

.PHONY: run # 	Run application with python -m boardgame.main
run: 
	python -m boardgame.main

.PHONY: format # 	Format PEP8 code style usin black and isort
format:
	@isort  boardgame
	python -m black boardgame

.PHONY: test # 	Run test with pytest and coverage boardgane
test:
	python -m pytest --cov=boardgame

.PHONY: test-cov # 	Run pytest with corverage report in html
test-cov:
	python -m pytest --cov=boardgame --cov-report html

.PHONY: build # 	Buider Dockerfile board:latest
build:
	docker build -t board:latest . 

.PHONY: drun # 	Run container builded 
drun:
	docker container run board:latest