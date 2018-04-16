import boto3


def session(
    aws_access_key_id=None,
    aws_secret_access_key=None,
    profile_name=None
):
    return boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        profile_name=profile_name)


def client(
    service_name,
    aws_access_key_id=None,
    aws_secret_access_key=None,
    profile_name=None
):
    return session(
        aws_access_key_id,
        aws_secret_access_key,
        profile_name
    ).client(service_name)


def resource(
    service_name,
    aws_access_key_id=None,
    aws_secret_access_key=None,
    profile_name=None
):
    return session(
        aws_access_key_id,
        aws_secret_access_key,
        profile_name
    ).resource(service_name)

