from setuptools import setup, find_packages
from os import path

with open("README.md") as f:
    readme = f.read()

setup(
    name='compiler',
    long_description=readme,
    packages=["hm", "lexer", "semantic", "syntatic"]
)