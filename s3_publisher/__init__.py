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
    '-k', '--aws-key',
    dest='AWS_KEY',
    type=str,
    help='AWS IAM user API key'
)

parser.add_argument(
    '-s', '--aws-secret-key',
    dest='AWS_SECRET_KEY',
    type=str,
    help='AWS IAM user secret API key'
)

parser.add_argument(
    '-p', '--profile',
    type=str,
    help='Preconfigured AWS CLI profile'
)

def main():
    args = parser.parse_args()
    print("Hey, s3-publisher here, and I'm working, everyone!")

    uploader = Uploader()
    uploader.upload(
        args.path,
        args.bucket
    )

