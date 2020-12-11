DATE=$(shell date +%F%T)

run:
	mkdir ./tests
	cp -rf WtfPy/* ./tests
	wget https://raw.githubusercontent.com/Zyycyx/wtfpy/master/testing/V0.0.2/test.py -P ./tests
	python tests/test.py 
	python tests/test.py > logs/tests/test_$(DATE).log
	rm -rf ./tests
build:
	sudo python3 setup.py sdist
