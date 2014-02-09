import random

import pygame
from pygame.locals import *
from igraph import *

from display.colors import *
from display.node import *
from display.inputbox import *

class App:
    """
        Class:
            Main Application draws graph animation
        """

    def __init__(self, width, height, graph_layout, filename):
        self._running = True
        self.screen = True
        self.size = self.width, self.height = width, height
        self.clock = pygame.time.Clock()
        self.graph = Graph()
        self.nodes = []
        self.margin = 20
        self.filename = filename
        self.graph_layout = graph_layout        
        self.inputbox = InputBox("Search", self.margin+200, self.height - (self.margin+20), 200, 20 )
        self.btn_rect = self.inputbox.button.rect
        print self.btn_rect

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, 
                             pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        print "App initialized, window size: ", self.width, self.height

        self.screen.fill(gray)
        pygame.display.flip()
        
        try:
            print "loading ", self.filename
            self.graph = load(self.filename)
        except:
            print "Couldn't load data file"
            self._running = False
            return

        l = self.graph.layout(self.graph_layout)
        l.fit_into( BoundingBox(self.width-(self.margin*2), self.height-(self.margin*2)) )
        self.graph.vs["coords"] = l.coords
        
        for i, v in enumerate(self.graph.vs):
            xpos = random.randrange(self.margin, self.width-self.margin, 1)
            ypos = random.randrange(self.margin, self.height-self.margin, 1)
            node = Node(i, xpos, ypos)
            node.target = ( round(self.graph.vs[i]["coords"][0])+self.margin, round(self.graph.vs[i]["coords"][1])+self.margin )
            self.nodes.append(node)
            

    def on_event(self, event):
        if event.type == pygame.QUIT:
            print "App quitting"
            self._running = False
        elif event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                self.inputbox.current_message = self.inputbox.current_message[0:-1]
            elif event.key == K_RETURN:
                pass
            elif event.key <= 127:
                self.inputbox.current_message = self.inputbox.current_message + chr(event.key)
            if event.key == K_ESCAPE:
                self._running = False
        elif event.type == MOUSEBUTTONUP and event.button == 1:
            x,y = event.pos
            print "You released the left mouse button at (%d, %d)" % event.pos      
            if self.btn_rect.collidepoint(x, y):
                print "You clicked inside the box"
       
    def on_render(self):
        self.clock.tick(30)
        pygame.display.set_caption("fps: " + str(self.clock.get_fps()))
        self.screen.fill(gray)
        for e in self.graph.es:        
            src_idx = e.source
            dest_idx = e.target
            s_x = max(0, min(self.nodes[src_idx].trueX, self.width)) 
            s_y = max(0, min(self.nodes[src_idx].trueY, self.height)) 
            d_x = max(0, min(self.nodes[dest_idx].trueX, self.width)) 
            d_y = max(0, min(self.nodes[dest_idx].trueY, self.height)) 
            pygame.draw.line( self.screen, medgray, (s_x, s_y), (d_x, d_y) )  
        for node in self.nodes:
            node.update()
            pygame.draw.ellipse(self.screen, blue, node.rect )            
        self.inputbox.display_box(self.screen)
        pygame.display.flip()


    def on_execute(self):
        print "App executing"
        if self.on_init() == False:
            self._running = False
        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


    def on_loop(self):
        pass


    def on_cleanup(self):
        print "App cleaning up"
        pygame.quit()


if __name__ == "__main__":
    theApp = App(1024, 768, "kamada_kawai", "data/file.pickle")
    theApp.on_execute()

