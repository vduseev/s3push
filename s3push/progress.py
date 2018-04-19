import threading
import sys
import os

class ProgressPercentage(object):

    def __init__(self, size):
        self._size = size
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify we'll assume this is hooked up
        # to a single filename.
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\rUploading: %s / %s  (%.2f%%)" % (
                    self._seen_so_far,
                    self._size,
                    percentage)
            )
            sys.stdout.flush()



