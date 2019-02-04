"""
Mercury main application.
Intended to be used as Polaris test application.
Reads geojson files from disk and sends them Polaris via HTTP.
"""

import argparse
import logging

from endpoints import PolarisAPI
from file_reader import read_file
from polaris_client import PolarisClient

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)

parser = argparse.ArgumentParser(description='Mercury. Sends GeoJSON or TCX files to Polaris server.')
parser.add_argument('--file', dest='file', help='The file to send')
parser.add_argument('--type', dest='type', help='Type of file to send (geojson/tcx)', default='geojson')
parser.add_argument('--server', dest='server_address', help='URL of the Polaris server where to send the data', default='http://127.0.0.1:3000/')
args = parser.parse_args()

if not args.file:
    parser.print_help()
    exit()

logging.debug("Mercury starting.")
data = read_file(args.file)
if data is not None:
    logging.debug("Sending " + args.file + " to Polaris server at " + args.server_address)
    if args.type == 'geojson':
        endpoint = PolarisAPI.geojson.value
    if args.type == 'tcx':
        endpoint = PolarisAPI.tcx.value
    client = PolarisClient(args.server_address)
    client.send_data(data, endpoint)

logging.debug("Mercury finished.")
