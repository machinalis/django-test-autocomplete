#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('README.rst') as readme:
    __doc__ = readme.read()

from distutils.core import setup

setup(
    name='django-test-autocomplete',
    version='0.1.1',
    description=u'A bash-autocomplete helper that list TestCases and tests',
    long_description=__doc__,
    author = u'Javier Mansilla',
    author_email = 'jmansilla@machinalis.com',
    url='https://github.com/machinalis/django-test-autocomplete',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
      ],
    scripts=['djntest', 'get_testcases_helper/get_testcases.py']
)
