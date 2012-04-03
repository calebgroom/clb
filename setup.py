#!/usr/bin/env python
# -*- encoding: utf-8 -*-
__author__ = "Caleb Groom <caleb@calebgroom.com>"
import os
from setuptools import setup, find_packages

NAME = "clb"
GITHUB_URL = "https://github.com/calebgroom/%s" % (NAME)
DESCRIPTION = "Command-line tool for Rackspace Load Balancers"
VERSION = "0.0.1"


def read(fname):
    full_path = os.path.join(os.path.dirname(__file__), fname)
    if os.path.exists(fname):
        return open(full_path).read()
    else:
        return ""

requirements = ['python-cloudlb', 'httplib2', 'argparse', 'prettytable']

setup(name=NAME,
      version=VERSION,
      download_url="%s/zipball/%s" % (GITHUB_URL, VERSION),
      description=DESCRIPTION,
      author='Caleb Groom',
      author_email='caleb@calebgroom.com',
      url=GITHUB_URL,
      long_description=read('README.rst'),
      license='BSD',
      include_package_data=True,
      zip_safe=False,
      scripts=['bin/clb'],
      packages=find_packages(exclude=['tests', 'debian']),
      install_requires=requirements,
      tests_require=["nose"],
      test_suite="nose.collector",
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Distributed Computing',
        'Topic :: Utilities',
        ],
      )
