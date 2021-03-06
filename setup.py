#!/usr/bin/env python

from setuptools import setup, find_packages
from os import path


def package_env(file_name, strict=False):
    file_path = path.join(path.dirname(__file__), file_name)
    if path.exists(file_path) or strict:
        return open(file_path).read()
    else:
        return ''

VERSION = package_env('VERSION')


if __name__ == '__main__':
    setup(
        name='UISoup',
        version=VERSION,
        description='Library for UI testing.',
        long_description=package_env('README.rst'),
        author='Max Beloborodko',
        author_email='f1ashhimself@gmail.com',
        packages=['uisoup'] + ['.'.join(('uisoup', p)) for p in
                               find_packages('uisoup')],
        include_package_data=True,
        install_requires=['selenium', 'comtypes'],
        zip_safe=False,
        entry_points={
            'console_scripts': [
                'ui-inspector = uisoup.ui_inspector:main'
            ]
        }
    )
