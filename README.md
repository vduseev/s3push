# s3-publisher 

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/91264fd782414d7c8c40d7e2dbc4254a)](https://www.codacy.com/app/vagiz.d/s3-publisher?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=vduseev/s3-publisher&amp;utm_campaign=Badge_Grade) 
[![CircleCI](https://circleci.com/gh/vduseev/s3-publisher/tree/master.svg?style=svg)](https://circleci.com/gh/vduseev/s3-publisher/tree/master)

Upload whole directories or distinct files to AWS S3 using `s3publish` in command line. Extensive support for different credential sources.

## Installation

Recommended installation method is via Pipenv:
```
pipenv install s3-publisher
```

Installing via Pip instead of Pipenv:
```
pip install s3-publisher
```

## Usage

**Publish a directory with default credentials**
```
s3publish ~/my-website/ example.com
```

**Publish a file using default credentials**
```
s3publish ~/my-website/index.html example.com
```

**Publish with provided key pair**
```
s3publish ~/my-website/ example.com -k XXXXXXXXXXXXXXXXXXXX -s xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 
```

**Publish with saved profile by providing its name**
```
s3publish ~/my-website/ example.com -p my-deployment-profile
```

**Note**: see [all possible](#priority-of-credentials-providers) options for specifying credentials below.

## Priority of credentials providers

1. Passing credentials as optional arguments: `-k AWS_ACCESS_KEY_ID, -s AAWS_SECRET_ACCESS_KEY`.
1. Passing profile name of pre-configured credentials as optional argument: `-p PROFILE_NAME`.
1. Environment variables, as listed in the [boto3 guide](http://boto3.readthedocs.io/en/latest/guide/configuration.html#environment-variable-configuration).
1. Default credentials in the shared credential file (`~/.aws/credentials`).
1. Default credentials in the AWS config file (`~/.aws/config`).
1. Boto2 config file (`/etc/boto.cfg` and `~/.boto`).

