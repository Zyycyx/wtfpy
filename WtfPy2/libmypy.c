#include <Python.h>
#include "libmypy.h"

PyObject * hello(PyObject * self) {
	return PyUnicode_FromFormat("[OK] WtfPy included!");
}

PyObject * getVal(PyObject *self, PyObject *args) {
	int num;
	char *name;

	if(!PyArg_ParseTuple(args, "is", &num, &name))
		return NULL;

	return PyUnicode_FromFormat("[VAR: %s]: %d.", name, num);
}
