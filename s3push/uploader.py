import os
import sys
import boto3
import logging

from s3push.progress import ProgressPercentage

log = logging.getLogger(__file__)


def upload(path, bucket, show_progress=False):
    path = os.path.realpath(path)
    srcdir = path if os.path.isdir(path) else os.path.dirname(path)
    callback = None  # for progress reporting

    # Measure size
    if show_progress:
        size = _measure(path)
        callback = ProgressPercentage(size)

    # Upload files to S3
    for f in _scan(path):
        local_path = f.path  # path of the file on the client machine
        # Path (key) under which the file will be stored in the bucket
        key_path = os.path.relpath(local_path, srcdir)
        bucket.upload_file(
            local_path,
            key_path,
            ExtraArgs={'ACL': 'public-read'},
            Callback=callback)


def _measure(path):
    size = 0
    for f in _scan(path):
        try:
            size += f.stat().st_size
        except Exception as ex:
            continue
    return size


def _upload_file(path, bucket, srcdir, callback=None):
    extra_args = { 'ACL': 'public-read' }
    local_path = path
    bucket_path = os.path.relpath(path, srcdir)

    log.debug('uploading %s to %s:%s', local_path, bucket.name, bucket_path)
    log.debug(bucket.upload_file(
        local_path,
        bucket_path,
        ExtraArgs=extra_args,
        Callback=callback))


def _scan(path):
    if os.path.isdir(path):
        yield from _scantree(path)
    elif os.path.isfile(path):
        yield from _scanfile(path)


def _scantree(path):
    """Recursively yield DirEntry objects for given directory."""
    for entry in os.scandir(path):
        if entry.is_dir(follow_symlinks=False):
            yield from _scantree(entry.path)
        else:
            yield entry


def _scanfile(path):
    "Yield DirEntry object for a single file"
    directory, filename = os.path.split(path)
    yield from filter(
        lambda obj: obj.name == filename,
        os.scandir(directory))

