DATE=$(shell date +%F%T)

run:
	mkdir ./tests
	cp -rf WtfPy/* ./tests
	wget https://raw.githubusercontent.com/Zyycyx/wtfpy/master/testing/V0.0.2/test.py -P ./tests
	python3.8 tests/test.py 
	python3.8 tests/test.py > logs/tests/test_$(DATE).log
	rm -rf ./tests
build:
	sudo python3.8 setup.py sdist
