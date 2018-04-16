import logging

log = logging.getLogger(__file__)


def erase(bucket):
    for key in bucket.objects.all():
        key.delete()

