# coding:utf-8
from setuptools import setup, find_packages

packages = find_packages('worksystem')
print(packages)

setup(
    name='worksystem',
    version='0.1',
    decription='work system',
    author='jummy, nishuidey',
    author_email='a929440925@gmail.com',
    url='http://127.0.0.1:8000',
    packages=packages,
    packages_dir={'', 'wordsystem'},
    include_package_data=True,
    install_requires=[
        'django==2.0.5',
        'python-decouple-3.1',
    ],
    scripts=[
        'worksystem/manage.py',
    ],
)
