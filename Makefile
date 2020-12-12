VERSION=V0.0.2
DATE=$(shell date +%F%T)

ifeq (, $(shell which python ))
  $(error "PYTHON=$(PYTHON) not found in $(PATH)")
endif

PYTHON_VERSION_MIN=3.6
PYTHON_VERSION=$(shell $(PYTHON) -c 'import sys; print("%d.%d"% sys.version_info[0:2])' )
PYTHON_VERSION_OK=$(shell $(PYTHON) -c 'import sys;\
  print(int(float("%d.%d"% sys.version_info[0:2]) >= $(PYTHON_VERSION_MIN)))' )

ifeq ($(PYTHON_VERSION_OK),0)
  $(error "Need python $(PYTHON_VERSION) >= $(PYTHON_VERSION_MIN)")
endif

test-online:
	mkdir ./tests
	cp -rf WtfPy/* ./tests
	wget https://raw.githubusercontent.com/Zyycyx/wtfpy/master/testing/$(VERSION)/test.py -P ./tests
	python tests/test.py 
	python tests/test.py > logs/tests/test_$(DATE).log
	rm -rf ./tests

test-local:
	mkdir ./tests
	cp -rf WtfPy/* ./tests
	cp -rf ./testing/$(VERSION)/test.py ./tests/ 
	python tests/test.py 
	python tests/test.py > logs/tests/test_$(DATE).log
	rm -rf ./tests
build_package:
	rm dist/*
	python setup.py build
	python setup.py clean
	python setup.py sdist
	python setup.py bdist
	python setup.py bdist_dumb
	python setup.py bdist_rpm

	
