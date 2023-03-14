import argparse
from bs4 import BeautifulSoup as soup
import requests as req
import pandas as pd
from IPython.display import Image

# Create the argument parser
parser = argparse.ArgumentParser(description='Scrape a Goodreads Listopia list.')
parser.add_argument('url', metavar='url', type=str, help='URL of the Goodreads Listopia list to scrape')

# Parse the arguments
args = parser.parse_args()

# Set the URL to scrape from the command line argument
list_url = args.url