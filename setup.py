from setuptools import setup

with open("README.md") as f:
    readme = f.read()

setup(
    name='compiler',
    long_description=readme,
    packages=["hm", "lexer", "semantic", "syntatic"]
)