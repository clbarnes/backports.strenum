#!/usr/bin/env python
import pathlib

from setuptools import setup, find_packages


here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.rst').read_text(encoding='utf-8')

setup(
    name='backports.strenum',  # Required
    version='0.1.0',  # Required
    description='Base class for creating enumerated constants that are also subclasses of str',  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/x-rst',  # Optional (see note above)
    url='https://github.com/clbarnes/backports.strenum',  # Optional
    author='Chris L. Barnes',  # Optional
    author_email='chrislloydbarnes@gmail.com',  # Optional
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='backports, enum, strenum',  # Optional
    packages=find_packages(exclude='tests'),  # Required
    test_suite="tests",
    python_requires='>=3.6, <4',
)
