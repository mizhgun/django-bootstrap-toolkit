# -*- coding: utf-8 -*

import os
import re
from setuptools import setup

# Read version from file
VERSION_FILE = 'bootstrap_toolkit/_version.py'
version_text = open(VERSION_FILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, version_text, re.M)
if mo:
    version = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSION_FILE,))


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='django2-bootstrap-toolkit',
    version=version,
    url='https://github.com/mizhgun/django-bootstrap-toolkit',
    author='mizhgun',
    author_email='mizhgun@gmail.com',
    license='Apache License 2.0',
    packages=['bootstrap_toolkit', 'bootstrap_toolkit.templatetags'],
    include_package_data=True,
    description='Bootstrap 2 support for Django 2.x projects',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Environment :: Web Environment",
        "Framework :: Django",
    ],
)
