# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in misc/__init__.py
from misc import __version__ as version

setup(
	name='misc',
	version=version,
	description='Random functionality based on ERPNext',
	author='Ebuka Akeru ',
	author_email='ebukaakeru@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
