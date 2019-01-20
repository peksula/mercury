import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from geojson_reader import GeoJsonReader

class GeoJsonReading(unittest.TestCase):
    def setUp(self):
        self.reader = GeoJsonReader()

    def test_reading_nonexisting_file_fails(self):
        geojson = self.reader.read_gjson_file("nonexisting")
        self.assertIsNone(geojson)

    def test_reading_geojson_file_succeeds(self):
        path_to_test_file = os.path.join(os.path.dirname(__file__), 'sample_1', 'routes.geojson')
        expected_content = """{
"type": "FeatureCollection",
"name": "routes",
"crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
"features": [

]
}
"""
        geojson = self.reader.read_gjson_file(path_to_test_file)
        self.assertIsNotNone(geojson)
        self.assertEquals(geojson, expected_content)

if __name__ == '__main__':
    unittest.main()