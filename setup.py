#!/usr/bin/env python
from setuptools import setup

NAME = "cloudage"
setup(
    name=NAME,
    use_scm_version={
        "local_scheme": "dirty-tag",
        "write_to": f"{NAME}/_version.py",
        "fallback_version": "0.0.0",
    },
    author="Ross Fenning",
    author_email="github@rossfenning.co.uk",
    packages=[NAME],
    description="Converts AWS CloudFormation to Graphviz DOT.",
    install_requires=["setuptools"],
    setup_requires=[
        "setuptools_scm>=3.3.1",
        "pre-commit",
    ],
    extras_require={
        "test": [
            "pytest",
            "pytest-pikachu",
            "pytest-mypy",
        ],
    },
    entry_points={
        "console_scripts": [
            "cloudage = cloudage:main",
        ],
    },
)
