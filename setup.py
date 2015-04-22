#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [

]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pipreqs',
    version='0.1.0',
    description="Pip Requirements generator based on imports in project",
    long_description=readme + '\n\n' + history,
    author="Vadim Kravcenko",
    author_email='vadim.kravcenko@gmail.com',
    url='https://github.com/bndr/pipreqs',
    packages=[
        'pipreqs',
    ],
    package_dir={'pipreqs':
                 'pipreqs'},
    include_package_data=True,
    install_requires=requirements,
    license="Apache License 2.0",
    zip_safe=False,
    keywords='pip requirements imports',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    entry_points={
        'console_scripts': [
            'pipreqs = pipreqs.pipreqs:main',
        ],
    },
)