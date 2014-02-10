# gui.py

from inputbox import *
from button import *


class Gui:
    """
        Class:
            Draws GUI
        """

    def __init__(self, screen):
    	self.margin = 20
    	self.screen = screen
    	self.height = self.screen.get_height()
    	self.inputbox = InputBox("Search", self.margin+200, self.height - (self.margin), 200, 20 )
    	self.depthbox = InputBox("Depth", self.margin+320, self.height - (self.margin), 100, 20 )
    	self.button = Button("Go", self.margin+370, self.height - (self.margin), 25, 20 )
        self.btn_rect = self.button.rect        
        
    def draw_display(self,screen):
    	self.inputbox.display_box(screen)
    	self.depthbox.display_box(screen)
    	self.button.display_box(screen)