# graph.py
import random

from igraph import *
from network.network import *
from display.node import *


LEVELS = 3
DEPTH = 3
blacklist = ['disambiguation', 'note-', 'Template', 'edit', ':', 'commons' ]


class PiGraph:
    """
        Class:
            Main Application draws graph animation
        """

    def __init__(self, graph_layout, width, height, margin, keyword=None, filename=None):
        self.ig = Graph()
        self.ig_layout = graph_layout
        self.width = width
        self.height = height
        self.margin = margin
        self.keyword = keyword
        self.network = Network()
        self.filename = filename
  

    def add_vertex_with_attrs(self, attrs):
        n = self.ig.vcount()
        self.ig.add_vertex(name=attrs["name"])
        for key, value in attrs.iteritems():
            self.ig.vs[n][key] = value


    def create_graph(self):
        if self.filename:
            print "loading ", self.filename
            self.ig = load(self.filename)
        elif self.keyword:
            # level 0 (root)
            self.ig = Graph()   
            label = self.keyword.lower().replace('_', ' ')
            attr = { "name": label, 
                    "label": label, 
                    "level": 0, 
                    "href":'http://en.wikipedia.org/wiki/'+self.keyword                 
                     }
            self.add_vertex_with_attrs(attr)
            print "added vertice 0, " + label
            # levels > 0
            prev_level_start = 0
            for level in range(1, LEVELS):
                prev_level_end = self.ig.vcount()
                for i in range(prev_level_start, prev_level_end):       
                    parent_label = self.ig.vs[i]["label"]           
                    child_links = self.network.get_links_from_url(self.ig.vs[i]["href"])
                    link_count = 0
                    for link in child_links:
                        if link_count < DEPTH and not any(word in link['href'] for word in blacklist):
                            label = link['href'][6:40].lower().replace('_', ' ')
                            try:
                                node = self.ig.vs.find(label)
                                self.ig.add_edges( [(i,node)] )
                                print "Repeated node: ", label, ", adding edge (", i, node.index, ")"
                            except ValueError:                                      
                                # add node to graph, add edge to parent
                                attr = { "name": label, 
                                        "label": label, 
                                        "level": level, 
                                        "href":'http://en.wikipedia.org' + link['href']
                                        }
                                self.add_vertex_with_attrs(attr)                   
                                idx = self.ig.vcount()-1
                                self.ig.add_edges( [ (i, idx)] )
                                print "New node: " + label + ", index: " + str(idx) + ", edge ( "+ str(i) +", " + str(idx) + " )"                   
                            link_count += 1 
                prev_level_start = prev_level_end
                prev_level_end = self.ig.vcount()


    def find_nodes(self):   
        self.create_graph()
        l = self.ig.layout(self.ig_layout)
        l.fit_into( BoundingBox(self.width-(self.margin*2), self.height-(self.margin*2)) )
        self.ig.vs["coords"] = l.coords

        nodes = []
        for i, v in enumerate(self.ig.vs):
            xpos = random.randrange(self.margin, self.width-self.margin, 1)
            ypos = random.randrange(self.margin, self.height-self.margin, 1)
            node = Node(i, xpos, ypos)
            node.target = ( round(self.ig.vs[i]["coords"][0])+self.margin, round(self.ig.vs[i]["coords"][1])+self.margin )
            nodes.append(node)
        return nodes


    def save_graph(self, save_filename):
        try:
            self.ig.save(save_filename) 
            print "Saved file ", save_filename
        except:
            print "Error saving file"

