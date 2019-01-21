"""
Reads a geojson file from disk.
"""

import os
import logging
import sys

class GeoJsonReader(object):

    def __init__(self):
        """
        Constructor.
        """
        pass

    def read_gjson_file(self, file_name):
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

    def _validate(self, geo_json):
        """
        Validates given geojson content against schema
        """
        raise NotImplementedError
