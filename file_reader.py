"""
Reads a file from disk.
"""

import os
import logging
import sys

def read_file(file_name):
    """
    Reads given file into memory.
    Returns file content, or None in case of an error.
    """
    try:
        content = open(file_name).read()
    except IOError:
        logging.error("Could not read file " + file_name)
        content = None
    return content
