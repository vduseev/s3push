# s3push

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/91264fd782414d7c8c40d7e2dbc4254a)](https://www.codacy.com/app/vagiz.d/s3push?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=vduseev/s3push&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.org/vduseev/s3push.svg?branch=master)](https://travis-ci.org/vduseev/s3push)
[![PyPI version](https://badge.fury.io/py/s3push.svg)](https://badge.fury.io/py/s3push)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Upload whole directories or distinct files to AWS S3 using `s3push` in command line. Extensive support for different credential sources.

## Project goal

This tool facilitates painless upload of directories to AWS S3. The initial goal was to provide developers with a simple tool that allows them to upload whole directories to S3 with a minimal effort. Initial project vision also contained an option to create and configure a fresh S3-hosted website from scratch.

However, the tool has been written after a very quick research and, as a result, suffered from the *"Not invented here"* syndrome. After a bit more careful research it was discovered that not only the other directory uploading tools exist, but also that there are far more superior instruments that also allow configuration of buckets and CloudFront CDN (i.e., `s3cmd`). See the rough [feature set comparison](docs/feature_set_comparison.pdf) in the docs.

As a **project's post-mortem**, it can be concluded that a proper research must be performed prior to the start of development. For example, before developing a new library or a tool it may be very useful to make a simple feature set comparison.

The project will, however, continue to exist as a demonstration of continuous delivery setup for a python package development. The environment for the project is designed to support fully automated releases and testing.

## Installation

Recommended installation method is via Pipenv:
```console
pipenv install s3push
```

Installing via Pip instead of Pipenv:
```console
pip install s3push
```

## Usage

**Publish a directory with default credentials**
```console
s3push ~/my-website/ example.com
```

**Publish a file using default credentials**
```console
s3push ~/my-website/index.html example.com
```

**Publish with provided key pair**
```console
s3push ~/my-website/ example.com -k XXXXXXXXXXXXXXXXXXXX -s xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**Publish with saved profile by providing its name**
```console
s3push ~/my-website/ example.com -p my-deployment-profile
```

**Note**: see [all possible](#priority-of-credentials-providers) options for specifying credentials below.

## Priority of credentials providers

1. Passing credentials as optional arguments: `-k AWS_ACCESS_KEY_ID, -s AAWS_SECRET_ACCESS_KEY`.
1. Passing profile name of pre-configured credentials as optional argument: `-p PROFILE_NAME`.
1. Environment variables, as listed in the [boto3 guide](http://boto3.readthedocs.io/en/latest/guide/configuration.html#environment-variable-configuration).
1. Default credentials in the shared credential file (`~/.aws/credentials`).
1. Default credentials in the AWS config file (`~/.aws/config`).
1. Boto2 config file (`/etc/boto.cfg` and `~/.boto`).

## Continuous Delivery

| Branch | Travis-CI Status | CircleCI Status |
| - | - | - |
| master | [![Build Status](https://travis-ci.org/vduseev/s3push.svg?branch=master)](https://travis-ci.org/vduseev/s3push) | [![CircleCI](https://circleci.com/gh/vduseev/s3push/tree/master.svg?style=shield)](https://circleci.com/gh/vduseev/s3push/tree/master) |
| dev | [![Build Status](https://travis-ci.org/vduseev/s3push.svg?branch=dev)](https://travis-ci.org/vduseev/s3push) | [![CircleCI](https://circleci.com/gh/vduseev/s3push/tree/dev.svg?style=shield)](https://circleci.com/gh/vduseev/s3push/tree/dev) |

