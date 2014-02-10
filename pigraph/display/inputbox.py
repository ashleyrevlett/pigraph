# based on code by Timothy Downs
# refactored by ar to be class based
# It ignores the shift key
# And, for reasons of my own, this program converts "-" to "_"
# allows backspace
# Called by:
# import inputbox
# box = inputbox.inputbox(screen, "Question", x, y, width, height)
# answer = box.ask()


import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *

from button import *

class InputBox:

	def __init__(self, question, x, y, width, height):
		if not pygame.font.get_init():
		  pygame.font.init()
		self.question = question
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.screen = pygame.display.get_surface()
		self.question = question
		self.button = Button("Go", self.x+50, self.y, 30, self.height)
		self.current_message = ""
		self.fontobject = pygame.font.Font(None,18)
		self.label = self.fontobject.render(self.question, 1, (200,200,20))

	def display_box(self, screen):
		""" called by on_render """	
		# draw label
		screen.blit(self.label, (self.x-self.width, self.y - self.height))

		pygame.draw.rect(screen, (255,255,255), (self.x - self.width + self.fontobject.size(self.question)[0] + 10, self.y - self.height,
						self.width-self.fontobject.size(self.question)[0],self.height), 0)
		if len(self.current_message) != 0:
			screen.blit(self.fontobject.render(self.current_message, 1, (60,60,60)),
						(self.x - self.width + self.fontobject.size(self.question)[0] + 15, self.y - self.height + 3))
		self.button.display_box(screen)

