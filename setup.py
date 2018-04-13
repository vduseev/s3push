from setuptools import setup, find_packages

from os import path
from codecs import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# with open(os.path.join(mypackage_root_dir, 'VERSION')) as version_file:
    # version = version_file.read().strip()

setup(
    name='s3-publisher',
    version='1.0.0b1',
    description='Upload directories to AWS S3',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/vduseev/s3-publisher',
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
            's3publish=s3_publisher:main',
        ]
    }
)
