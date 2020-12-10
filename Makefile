DATE=$(shell date +%F%T)

run:
	cp -rf WtfPy/* ./tests
	python3.8 tests/run.py 
	python3.8 tests/run.py > tests/logs/run_$(DATE).log
	rm -rf tests/.gitignor tests/config.txt tests/WtfPy.py tests/__main__.py tests/__init__.py  tests/__pycache__

build:
	sudo python3.8 setup.py sdist
