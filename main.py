"""
Mercury main application.
Intended to be used as Polaris test application.
Reads geojson files from disk and sends them Polaris via HTTP.
"""

import argparse
import logging

from geojson_reader import GeoJsonReader
from polaris_client import PolarisClient

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)

parser = argparse.ArgumentParser(description='Mercury. Sends GeoJSON files to Polaris server.')
parser.add_argument('--file', dest='geojson_file', help='The GeoJSON file to send')
parser.add_argument('--server', dest='server_address', help='URL of the Polaris server where to send geoJson', default='http://127.0.0.1:3000/')
args = parser.parse_args()

if not args.geojson_file:
    parser.print_help()
    exit()

logging.debug("Mercury starting.")
geojson = GeoJsonReader().read_gjson_file(args.geojson_file)
if geojson is not None:
    logging.debug("Sending " + args.geojson_file + " to Polaris server at " + args.server_address)
    PolarisClient(args.server_address).send_route(geojson)

logging.debug("Mercury finished.")
