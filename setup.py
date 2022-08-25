#!/usr/bin/env python
import pathlib

from setuptools import setup, find_packages


here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.rst").read_text(encoding="utf-8")

setup(
    name="backports.strenum",
    description="Base class for creating enumerated constants that are also subclasses of str",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/clbarnes/backports.strenum",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        # "Programming Language :: Python :: 3.6",
        # "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    keywords="backports, enum, strenum",
    packages=find_packages(exclude="tests"),
    package_data={"backports.strenum": ["__init__.pyi", "py.typed"]},
    test_suite="tests",
    python_requires=">=3.8, <4",
)
