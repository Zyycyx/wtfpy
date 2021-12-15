VERSION=V0.0.2
DATE=$(shell date +%F%T)

# For testing on Win10 WSL it's unusable 
#ifeq (, $(shell which python ))
#  $(error "PYTHON=$(PYTHON) not found in $(PATH)")
#endif

PYTHON_VERSION_MIN=3.8
PYTHON_VERSION=$(shell $(PYTHON) -c 'import sys; print("%d.%d"% sys.version_info[0:2])' )
PYTHON_VERSION_OK=$(shell $(PYTHON) -c 'import sys;\
  print(int(float("%d.%d"% sys.version_info[0:2]) >= $(PYTHON_VERSION_MIN)))' )

ifeq ($(PYTHON_VERSION_OK),0)
  $(error "Need python $(PYTHON_VERSION) >= $(PYTHON_VERSION_MIN)")
endif

run-buildserver:
	git pull
	mkdir ./tests
	cp -rf WtfPy/* ./tests
	wget https://raw.githubusercontent.com/Zyycyx/wtfpy/master/testing/$(VERSION)/test.py -P ./tests
	python tests/test.py 
	#python tests/test.py > logs/tests/test_$(DATE).log
	rm -rf ./tests
	
run-online:
	mkdir ./tests
	cp -rf WtfPy/* ./tests
	wget https://raw.githubusercontent.com/Zyycyx/wtfpy/master/testing/$(VERSION)/test.py -P ./tests
	python3 tests/test.py 
	#python3 tests/test.py > logs/tests/test_$(DATE).log
	rm -rf ./tests

run-local:
	mkdir ./tests
	cp -rf WtfPy/* ./tests
	cp -rf ./testing/$(VERSION)/test.py ./tests/ 
	python3 tests/test.py 
	#python3 tests/test.py > logs/tests/test_$(DATE).log
	rm -rf ./tests
build_package:
	rm dist/*
	python3 setup.py build
	python3 setup.py sdist
	python3 setup.py bdist
	python3 setup.py bdist_dumb
	python3 setup.py bdist_rpm
	mv dist/* ./manpackages
	python3 setup.py sdist bdist_wheel
	python3 setup.py clean
	
upload_test:
	twine upload --repository testpypi dist/*
publish:
	twine upload dist/*
