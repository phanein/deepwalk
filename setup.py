#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='deepwalk',
    version='1.0.1',
    description='DeepWalk online learning of social representations.',
    long_description=readme + '\n\n' + history,
    author='Bryan Perozzi',
    author_email='bperozzi@cs.stonybrook.edu',
    url='https://github.com/phanein/deepwalk',
    packages=[
        'deepwalk',
    ],
    entry_points={'console_scripts': ['deepwalk = deepwalk.__main__:main']},
    package_dir={'deepwalk':
                 'deepwalk'},
    include_package_data=True,
    install_requires=requirements,
    license="GPLv3",
    zip_safe=False,
    keywords='deepwalk',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
