#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("requirements.txt") as f:
    requirements = f.readlines()


setup(
    author="Rivo Laks",
    author_email="code@rivolaks.com",
    description="Advent of Code 2021",
    install_requires=requirements,
    long_description=readme,
    name="aoc2021",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    test_suite="tests",
    # Prevent accidental uploads to PyPI
    classifiers=["Private :: Do Not Upload"],
)
