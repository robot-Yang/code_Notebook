#!/usr/bin/env python

"""
setup.py file for SWIG C\+\+/Python example
"""
from distutils.core import setup, Extension

Yamahack_module = Extension('_Yamahack',
    sources=['Yamahack.cpp', 'Yamahack_wrap.cxx',],
)
setup (
    name = 'Yamahack',
    version = '0.1',
    author = "www.99fang.com",
    description = """Yamahack swig C\+\+/Python example""",
    ext_modules = [Yamahack_module],
    py_modules = ["Yamahack"],
)