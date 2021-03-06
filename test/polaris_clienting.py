import os
import sys
import requests
import unittest
from mock import patch, MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from polaris_client import PolarisClient

def _raise_for_status():
    raise requests.exceptions.HTTPError("Fake error")

class PolarisClienting(unittest.TestCase):
    def setUp(self):
        self.client = PolarisClient("fake_server_url/")
        self.payload = "{\"route\": \"fake_route\"}"

    @patch('requests.post', autospec=True)
    def test_sending_geojson_succeeds(self, mock_post):
        return_value = self.client.send_data(self.payload, 'api/geojson')
        mock_post.assert_called_with("fake_server_url/api/geojson", json=self.payload)
        self.assertTrue(return_value)

    @patch('requests.post', autospec=True)
    def test_sending_geojson_fails_can_not_connect(self, mock_post):
        fake_response = MagicMock()
        fake_response.status_code = 504
        fake_response.raise_for_status = _raise_for_status
        mock_post.return_value = fake_response

        return_value = self.client.send_data(self.payload, 'api/geojson')
        mock_post.assert_called_with("fake_server_url/api/geojson", json=self.payload)
        self.assertFalse(return_value)

if __name__ == '__main__':
    unittest.main()