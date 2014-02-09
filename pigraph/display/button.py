# button.py

import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *


class Button:

	def __init__(self, text, x, y, width, height):
		if not pygame.font.get_init():
		  pygame.font.init()
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.text = text
		self.padding = 3
		self.fontobject = pygame.font.Font(None,18)
		self.rect = Rect(x-width, y-height, width, height)

	def display_box(self, screen):
	  "Print a message in a box on the screen"	  
	  pygame.draw.rect(screen, (0,0,0),
					   (self.x - self.width,
						self.y - self.height,
						self.width,self.height), 0)
	  
	  if len(self.text) != 0:
		screen.blit(self.fontobject.render(self.text, 1, (200,200,200)),
					(self.x - self.width + self.padding, self.y - self.height + self.padding))	  



