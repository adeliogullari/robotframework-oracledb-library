#!/usr/bin/env python

import re
from os.path import abspath, dirname, join
from setuptools import setup, find_packages

CURDIR = dirname(abspath(__file__))

CLASSIFIERS = '''
Development Status :: 5 - Production/Stable
License :: OSI Approved :: Apache Software License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3 :: Only
Topic :: Software Development :: Testing
Framework :: Robot Framework
Framework :: Robot Framework :: Library
'''.strip().splitlines()

with open(join(CURDIR, 'src', 'OracleDBLibrary', '__init__.py')) as f:
    VERSION = re.search('\n__version__ = "(.*)"', f.read()).group(1)
with open(join(CURDIR, 'README.md')) as f:
    DESCRIPTION = f.read()
with open(join(CURDIR, 'requirements.txt')) as f:
    REQUIREMENTS = f.read().splitlines()

setup(
    name='robotframework-oracledb-library',
    version=VERSION,
    description='Oracle database library for Robot Framework',
    long_description=DESCRIPTION,
    author='Abdullah Deliogullari',
    author_email='abdullahdeliogullari@yaani.com',
    url='https://github.com/adeliogullari/robotframework-oracledb-library',
    license='Apache License 2.0',
    keywords='robotframework testing testautomation oracle database',
    platforms='any',
    classifiers=CLASSIFIERS,
    python_requires='>=3.6, <4',
    install_requires=REQUIREMENTS,
    package_dir={'': 'src'},
    packages=find_packages('src')
)
