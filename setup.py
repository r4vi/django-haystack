#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='django-haystack',
    version='2.0.4-pitchup-beta',
    description='Pluggable search for Django.',
    author='Daniel Lindsley, Pitchup.com',
    author_email='siteadmins@pitchup.com',
    long_description=open('README.rst', 'r').read(),
    url='http://haystacksearch.org/',
    install_requires=[
        'pysolr>=3.1.0'
        ],
    packages=[
        'haystack',
        'haystack.backends',
        'haystack.management',
        'haystack.management.commands',
        'haystack.templatetags',
        'haystack.utils',
    ],
    package_data={
        'haystack': [
            'templates/panels/*',
            'templates/search_configuration/*',
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)
