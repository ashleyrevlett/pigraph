# parser.py

from bs4 import BeautifulSoup
from network.network import *


class Parser:

    def __init__(self, keyword):
        self.blacklist = ['disambiguation', 'note-', 'Template', 'edit', ':', 'commons', 'wiktionary' ]
        self.keyword = keyword
        self.pagedata = ''
        self.network = Network()



    def get_related(self, keyword):
        """ retrieve links from network, 
        	parse them for the best links
        	@return list of 
        """

        self.pagedata = self.network.get_links(keyword)
        soup = BeautifulSoup(self.pagedata)
        all_links = soup.select("#mw-content-text a")
        links = []
        for link in all_links:
         if not any(word in link['href'].lower() for word in self.blacklist):
            links.append(link)
        return links        