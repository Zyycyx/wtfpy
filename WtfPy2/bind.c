#include "libmypy.h"

char hellofunc_docs[] = "Check if module is included";
char getvalfunc_docs[] = "To get a value runtime, with choosen name. ('FOR1', 'X')";

PyMethodDef WtfPy2_funcs[] = {
	{	"hello",
		(PyCFunction)hello,
		METH_NOARGS,
		hellofunc_docs},
	{	"getVal",
		(PyCFunction)getVal,
		METH_VARARGS,
		getvalfunc_docs},
	{	NULL}
};

char WtfPy2_docs[] = "WtfPy2 is a memory management module written with CPython.";

PyModuleDef WtfPy2_mod = {
	PyModuleDef_HEAD_INIT,
	"WtfPy2",
	WtfPy2_docs,
	-1,
	WtfPy2_funcs,
	NULL,
	NULL,
	NULL,
	NULL
};

PyMODINIT_FUNC PyInit_WtfPy2(void) {
	return PyModule_Create(&WtfPy2_mod);
}
