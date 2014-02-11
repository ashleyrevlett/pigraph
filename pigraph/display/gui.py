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
        self.levelsbox = InputBox("Levels", self.margin+440, self.height - (self.margin), 100, 20 )
    	self.inputboxes = [self.inputbox, self.depthbox, self.levelsbox]
        self.button = Button("Go", self.margin+500, self.height - (self.margin), 25, 20 )
        self.btn_rect = self.button.rect        
        self.inputbox.has_focus = True        
        
    def draw_display(self,screen):
        for box in self.inputboxes:
    	   box.display_box(screen)
    	self.button.display_box(screen)