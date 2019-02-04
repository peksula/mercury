import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from file_reader import read_file

class FileReading(unittest.TestCase):
    def setUp(self):
        pass

    def test_reading_nonexisting_file_fails(self):
        content = read_file("nonexisting")
        self.assertIsNone(content)

    def test_reading_file_succeeds(self):
        path_to_test_file = os.path.join(os.path.dirname(__file__), 'sample_1', 'routes.geojson')
        expected_content = """{
"type": "FeatureCollection",
"name": "routes",
"crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
"features": [

]
}
"""
        geojson = read_file(path_to_test_file)
        self.assertIsNotNone(geojson)
        self.assertEquals(geojson, expected_content)

if __name__ == '__main__':
    unittest.main()