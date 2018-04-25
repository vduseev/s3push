from setuptools import setup, find_packages

from os import path
from codecs import open
from datetime import date


def local_path(filename):
    return path.join(
        path.abspath(path.dirname(__file__)),
        filename)

# Get the long description from the README file
with open(local_path('README.md'), encoding='utf-8') as readme:
    long_description = readme.read()

# .build.info file must exist in the current directory and the
# build should fail if it does not.
# The file must contain build number in it.
with open(local_path('.build.info')) as build_info:
    build_number = build_info.read().strip()

today = date.today()
version = '{}.{}.{}'.format(today.year, today.month, build_number)

setup(
    name='s3push',
    version=version,
    description='Upload directories to AWS S3',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/vduseev/s3push',
    author='Vagiz Duseev',
    author_email='vagiz@duseev.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='aws s3 static website deployment directories folder upload push publish',
    packages=find_packages(),
    install_requires=['boto3'],
    extras_require={
        'dev': ['twine', 'wheels']
    },
    entry_points={
        'console_scripts': [
            's3push=s3push:main',
        ]
    }
)
