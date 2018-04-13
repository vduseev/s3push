import argparse
from s3_publisher.uploader import Uploader


parser = argparse.ArgumentParser()

parser.add_argument(
    'path',
    type=str,
    help='Path to a directory of file that needs to be uploaded'
)

parser.add_argument(
    'bucket',
    type=str,
    help='AWS S3 bucket name'
)

parser.add_argument(
    '-k', '--aws_access_key_id',
    dest='AWS_ACCESS_KEY_ID',
    type=str,
    default=None,
    help='AWS IAM user API key'
)

parser.add_argument(
    '-s', '--aws-secret-access-key',
    dest='AWS_SECRET_ACCESS_KEY',
    type=str,
    default=None,
    help='AWS IAM user secret API key'
)

parser.add_argument(
    '-p', '--profile-name',
    dest='PROFILE_NAME',
    type=str,
    default=None,
    help='Preconfigured AWS CLI profile'
)


def main():
    params = vars(parser.parse_args())

    print(params)

    uploader = Uploader()
    uploader.connect(params)
    uploader.upload(params)

