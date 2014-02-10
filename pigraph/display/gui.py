# gui.py

from inputbox import *


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
        self.btn_rect = self.inputbox.button.rect
        