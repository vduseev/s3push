import os
import sys
import threading
import mimetypes
from collections import namedtuple

import boto3

File = namedtuple('File', ['src_dir', 'rel_path'])

class Uploader(object):

    def __init__(self):
        self.name = 'uploader'

    def connect(self, profile_name=None):
        session = boto3.Session(profile_name)
        # Get the service client
        s3 = session.client('s3')
        return s3

    def upload(self, path, bucket_name):
        files = self.list_files(path)
        for f in files:
            self.upload_file(bucket_name, f)

    def upload_file(self, bucket_name, f):
        local_path = os.path.join(f.src_dir, f.rel_path)
        key = f.rel_path
        extra_args = { 
            'ContentType': self.guess_mime_type(local_path),
            'ACL': 'public-read'
        }
        print(local_path, key, extra_args)
        # s3.upload_file(
            # local_path,
            # bucket_name,
            # key,
            # Callback=None  # ProgressPercentage("tmp.txt")
        # )

    def guess_mime_type(self, path):
        mime, _ = mimetypes.guess_type(path)
        if mime is None:
            mime = 'text/plain'
        return mime

    def list_files(self, path):
        if os.path.isdir(path):
            for subdir_path, _, files in os.walk(path):
                for file_name in files:
                    full_path = os.path.join(subdir_path, file_name)
                    rel_path = os.path.relpath(full_path, path)
                    yield File(path, rel_path)
        elif os.path.isfile(path):
            src_dir, file_name = os.path.split(path)
            yield File(src_dir, file_name)

