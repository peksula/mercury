"""
Sends geojson data to Polaris server.
"""
import logging
import requests

from endpoints import PolarisAPI

class PolarisClient(object):

    def __init__(self, server_address):
        """
        Constructor.
        @param server_address Address of the Polaris server.
        """
        self._server_address = server_address

    def send_route(self, json_payload):
        """
        Sends given route to Polaris server.
        Returns True on success, False otherwise.
        """
        url = self._server_address + PolarisAPI.route.value
        try:
            response = requests.post(url, json=json_payload)
            response.raise_for_status() # raise an exception, if response comes back with some HTTP error code
        except requests.exceptions.RequestException  as err:
            logging.error("Sending route failed " + str(err))
            return False

        logging.debug("Route sent successfully to " + url)
        return True
