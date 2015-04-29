#!/usr/bin/env python

import os
from setuptools import setup


def read(readme_file):
    return open(os.path.join(os.path.dirname(__file__), readme_file)).read()


setup(
    name="cloudage",
    version="0.0.0",
    author='Ross Fenning',
    author_email='ross.fenning@gmail.com',
    packages=['cloudage'],
    description='Converts AWS CloudFormation to Graphviz DOT.',
    url='http://github.com/AvengerPenguin/cloudage',
    install_requires=['setuptools'],
    entry_points={
        'console_scripts': [
            'cloudage = cloudage:main',
        ],
    },
)
