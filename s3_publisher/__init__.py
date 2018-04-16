import logging
import argparse

from s3_publisher.connector import resource
from s3_publisher.uploader import upload


parser = argparse.ArgumentParser(
    description='Upload directories and files to AWS S3')

parser.add_argument(
    'path',
    type=str,
    help='Path to a directory of file that needs to be uploaded')

parser.add_argument(
    'bucket',
    type=str,
    help='AWS S3 bucket name')

parser.add_argument(
    '-k', '--aws_access_key_id',
    dest='AWS_ACCESS_KEY_ID',
    type=str,
    default=None,
    help='AWS IAM user API key')

parser.add_argument(
    '-s', '--aws-secret-access-key',
    dest='AWS_SECRET_ACCESS_KEY',
    type=str,
    default=None,
    help='AWS IAM user secret API key')

parser.add_argument(
    '-p', '--profile-name',
    dest='PROFILE_NAME',
    type=str,
    default=None,
    help='Preconfigured AWS CLI profile')

parser.add_argument(
    '--progress',
    action='store_true',
    help='Show upload progress bar')

parser.add_argument(
    '--log',
    type=str,
    default=logging.getLevelName(logging.WARNING),
    help='Show upload progress bar')


def main():
    params = parser.parse_args()

    logging.basicConfig(
        level=getattr(logging, params.log.upper()),
        format='%(asctime)s %(filename)20s %(levelname)8s %(message)s')

    s3 = resource(
        's3',
        params.AWS_ACCESS_KEY_ID,
        params.AWS_SECRET_ACCESS_KEY,
        params.PROFILE_NAME)
    bucket = s3.Bucket(params.bucket)
    upload(params.path, bucket, params.progress)

