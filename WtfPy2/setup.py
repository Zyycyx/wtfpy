#!/usr/bin/env python3

from distutils.core import setup, Extension

setup(
	name = "WtfPy2",
	version = "2.0",
	ext_modules = [Extension("WtfPy2", ["bind.c", "libmypy.c"])]
	);
