import os
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='PyScrapper',
    version='1.0',
    description='Python Scrapping interface',
    author='William Falcon',
    author_email='waf2107@columbia.edu',
    url='https://github.com/williamFalcon/PyScrapper.git',
    install_requires=required
)