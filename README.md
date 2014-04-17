pigraph
=======

__Pygame and igraph demo of wikipedia data graph__

Pigraph is a Wikipedia visualization project that builds a graph of related
Wikipedia pages. Enter a keyword, choose the number of levels of pages to
traverse, and the number of links on each page to use. Pygame is used to generate
an animated graph. iGraph is used for the graph position algorithm. Currently
the graph nodes are not interactive. 

Very much a work in progress, but stable enough to run.

**Required libraries:**
* [Pygame](http://www.pygame.org)
* [igraph](http://igraph.sourceforge.net/doc/python/igraph-module.html)
* [BeautifulSoup 4](http://www.crummy.com/software/BeautifulSoup/)
* [Requests](https://github.com/kennethreitz/requests)

**How to run:**
Install the libraries above, then in the command line:
```
git clone https://github.com/ashleyrevlett/pigraph.git
python pigraph/main.py
```

**Features under development:**
* Image export
* Detail view of node information
* Save tree for later
* Interactive addition of new nodes
