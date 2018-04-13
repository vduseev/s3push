import boto3
from collections import namedtuple


ConnectionMethod = namedtuple(
    'ConnectionMethod', 
    ['name', 'priority', 'is_valid', 'connect']
)

# Collection of methods to connect to AWS.
# Put into a list to avoid boilerplate code duplication.
_METHODS = [
    ConnectionMethod(
        'argument_key_pair', 1, # priority
        lambda params:
            params['AWS_ACCESS_KEY_ID'] and \
            params['AWS_SECRET_ACCESS_KEY'],
        lambda service, params:
            boto3.client(
                service,
                aws_access_key_id=params['AWS_ACCESS_KEY_ID'],
                aws_secret_access_key=params['AWS_SECRET_ACCESS_KEY']
            )
    ),
    ConnectionMethod(
        'argument_profile', 2, # priority
        lambda params:
            params['PROFILE_NAME'] is not None,
        lambda service, params:
            boto3.Session(
                profile_name=params['PROFILE_NAME']
            ).client(service),
    ),
    ConnectionMethod(
        'default', 3, # priority
        lambda params:
            True,
        lambda service, params:
            boto3.client(service)
     )
]

def connect(service_name, params):
    """
    Connects to specified AWS service using provided parameters.

    Tries different combination of parameters in order specified by
    _METHODS collection.
    """
    prioritized_methods = sorted(
        _METHODS,
        key=lambda method: method.priority
    )
    for method in prioritized_methods:
        if method.is_valid(params):
            return method.connect(service_name, params)

