import pygame
from pygame.locals import *
from igraph import *

from display.colors import *
from display.node import *
from display.gui import *
from pigraph.pigraph import *



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
        self.nodes = []
        self.margin = 20
        self.filename = filename
        self.graph_layout = graph_layout
        self.gui = True
        self.graph = True

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.gui = Gui(self.screen)
        self.graph = PiGraph(self.graph_layout, self.width, self.height, self.margin, filename=self.filename)        
        self._running = True
        self.screen.fill(gray)
        pygame.display.flip()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            print "App quitting"
            self._running = False
        elif event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                if self.gui.inputbox.has_focus:
                    self.gui.inputbox.current_message = self.gui.inputbox.current_message[0:-1]
                if self.gui.depthbox.has_focus:                    
                    self.gui.depthbox.current_message = self.gui.depthbox.current_message[0:-1]
            elif event.key == K_RETURN:
                pass
            elif event.key <= 127:
                if self.gui.inputbox.has_focus:
                    self.gui.inputbox.current_message = self.gui.inputbox.current_message + chr(event.key)
                if self.gui.depthbox.has_focus:                    
                    self.gui.depthbox.current_message = self.gui.depthbox.current_message + chr(event.key)                                    
            if event.key == K_ESCAPE:
                self._running = False
        elif event.type == MOUSEBUTTONUP and event.button == 1:
            x,y = event.pos
            print "You released the left mouse button at (%d, %d)" % event.pos   
            if self.gui.inputbox.rect.collidepoint(x,y):
                print "You clicked inside the input box"
                self.gui.inputbox.has_focus = True
                self.gui.depthbox.has_focus = False
            elif self.gui.depthbox.rect.collidepoint(x,y):
                print "You clicked inside the depthbox box"
                self.gui.inputbox.has_focus = False
                self.gui.depthbox.has_focus = True
            elif self.gui.btn_rect.collidepoint(x, y):
                print "You clicked inside the button"
                self.gui.inputbox.has_focus = False
                self.gui.depthbox.has_focus = False
                del self.graph
                self.graph = PiGraph(self.graph_layout, self.width, self.height, self.margin, depth=int(self.gui.depthbox.current_message), keyword=self.gui.inputbox.current_message)
                self.nodes = self.graph.find_nodes()


    def on_render(self):
        pygame.display.set_caption("fps: " + str(self.clock.get_fps()))
        self.screen.fill(gray)
        for e in self.graph.ig.es:        
            src_idx = e.source
            dest_idx = e.target
            s_x = max(0, min(self.nodes[src_idx].trueX, self.width)) 
            s_y = max(0, min(self.nodes[src_idx].trueY, self.height)) 
            d_x = max(0, min(self.nodes[dest_idx].trueX, self.width)) 
            d_y = max(0, min(self.nodes[dest_idx].trueY, self.height)) 
            pygame.draw.line( self.screen, medgray, (s_x, s_y), (d_x, d_y) )  
        for node in self.nodes:
            node.update()        
            x = node.trueX
            y = node.trueY
            level = self.graph.ig.vs[node.index]["level"]
            degree = self.graph.ig.degree(node.index)
            color = node.get_node_color(level)            
            pygame.draw.ellipse(self.screen, color, node.rect )            

            font_size = 9 + degree
            thisfont = pygame.font.SysFont('Arial', font_size)  
            label = thisfont.render(self.graph.ig.vs[node.index]['label'], 1, white)    
            label_x = int(max(min(x, self.width), 0))
            label_y = int(max(min(y, self.height), 0))        
            self.screen.blit(label, (label_x, label_y))    

        self.gui.draw_display(self.screen)
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
        self.clock.tick(30)


    def on_cleanup(self):
        print "App cleaning up"
        pygame.quit()


if __name__ == "__main__":
    theApp = App(1024, 768, "kamada_kawai", "data/file.pickle")
    theApp.on_execute()

