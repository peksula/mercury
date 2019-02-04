"""
Sends geojson data to Polaris server.
"""
import logging
import requests

class PolarisClient(object):

    def __init__(self, server_address):
        """
        Constructor.
        @param server_address Address of the Polaris server.
        """
        self._server_address = server_address

    def send_data(self, payload, endpoint):
        """
        Sends given GeoJSON to Polaris server.
        Returns True on success, False otherwise.
        """
        url = self._server_address + endpoint
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status() # raise an exception, if response comes back with some HTTP error code
        except requests.exceptions.RequestException  as err:
            logging.error("Sending failed " + str(err))
            return False

        logging.debug("Data sent successfully to " + url)
        logging.debug("Response " + response.text)
        return True
