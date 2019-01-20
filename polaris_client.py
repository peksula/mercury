"""
Sends geojson data to Polaris server.
"""
import logging
import sys
import urllib2

class PolarisClient(object):
    def __init__(self, url, timeout):
        self._url = url
        self._timeout = timeout

    def send_json(self, json_payload):
        req = urllib2.Request(self._url)
        req.add_header('Content-Type', 'application/json')
        try:
            response = urllib2.urlopen(req, json_payload, timeout=self._timeout)
        except urllib2.HTTPError, e:
            logging.error("Sending failed " + e.fp.read())
            return False

        logging.debug("Data sent successfully to " + self._url)
        return True
