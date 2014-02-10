# parser.py

import time

import requests
from bs4 import BeautifulSoup

class Network:
    """
        Class:
            Main Application draws graph animation
        """

    def __init__(self):
        pass

    def get_links_from_url(self, url):
        """ utility method to get all links from wiki url
        """
        r = requests.get(url)
        time.sleep(0.01) # be nice to wikipedia
        soup = BeautifulSoup(r.text)
        links = soup.select("#mw-content-text a")
        return links