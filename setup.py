"""Library Metadata Information."""

from setuptools import find_packages
from setuptools import setup

description = ('Configurable wrapper around Fynd APIs which helps '
               'to call Fynd APIs using function and classes.')

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='fdk_client',
    version='0.1.32',
    author='Manish Magnani',
    author_email='manishmagnani@gofynd.com',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/gofynd/fdk-client-python',
    packages=find_packages(
        exclude=('tests*', 'documentation', '_macros')),
    license='',
    install_requires=[
        "aiohttp>=3.8.0",
        "marshmallow>=3.12.2",
        "pytz>=2021.3",
        "ujson>=5.4.0",
    ],
    classifiers=[
        'Programming Language :: Python :: 3.8.2'
    ],
)
