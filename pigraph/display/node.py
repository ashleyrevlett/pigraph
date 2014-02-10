import pygame
from pygame.locals import *
from vector import *
from display.colors import *


class Node(pygame.sprite.Sprite):
    
    def __init__(self, index=0, x=0, y=0):
        '''
        Class:
            creates a sprite
        Parameters:
            - self
            - index
                index to use when accessing graph vertex sequence
            - x, y
                starting x and y pos to draw the node at
        '''
        # self.image = pygame.image.load("images/ornament_001.png").convert() # load image
        # self.rect = self.image.get_rect()

        self.radius = 4
        self.rect = Rect(0,0, self.radius*2, self.radius*2)
        self.trueX = x # created because self.rect.center does not hold
        self.trueY = y # decimal values but these do
        self.rect.center = (self.trueX, self.trueY) # set starting position
        self.speed = 5 # movement speed of the sprite
        self.speedX = 0 # speed in x direction
        self.speedY = 0 # speed in y direction
        self.normal_friction = .9 # friction while accelerating; lower = less springiness
        self.slowing_friction = .3 # friction while slowing down; lower = slows down faster
        self.index = index # used to access edgesequence
        self.target = None # starts off with no target

    def get_direction(self, target):
        '''
        Function:
            takes total distance from sprite.center
            to the sprites target
            (gets direction to move)
        Returns:
            a normalized vector
        Parameters:
            - self
            - target
                x,y coordinates of the sprites target
                can be any x,y coorinate pair in
                brackets [x,y] or parentheses (x,y)
        '''
        if self.target: # if the square has a target
            position = Vector(self.trueX, self.trueY) # create a vector from center x,y value
            target = Vector(target[0], target[1]) # and one from the target x,y
            self.dist = target - position # get total distance between target and position

            direction = self.dist.normalize() # normalize so its constant in all directions
            return direction
        
    def distance_check(self, dist):
        '''
        Function:
            tests if the total distance from the
            sprite to the target is smaller than the
            ammount of distance that would be normal
            for the sprite to travel
            (this lets the sprite know if it needs
            to slow down. we want it to slow
            down before it gets to its target)
        Returns:
            bool
        Parameters:
            - self
            - dist
                this is the total distance from the
                sprite to the target
                can be any x,y value pair in
                brackets [x,y] or parentheses (x,y)
        '''
        dist_x = dist[0] ** 2 # gets absolute value of the x distance
        dist_y = dist[1] ** 2 # gets absolute value of the y distance
        t_dist = dist_x + dist_y # gets total absolute value distance
        speed = self.speed ** 2 # gets aboslute value of the speed

        if t_dist <= (speed): # read function description above
            return True
        
    def update(self):
        '''
        Function:
            gets direction to move then applies
            the distance to the sprite.center
        Parameters:
            - self
        '''
        self.dir = self.get_direction(self.target) # get direction
        if self.dir: # if there is a direction to move
            
            if self.distance_check(self.dist): # if we need to slow down
                if self.speed > 1:
                    self.speed -= 1
                else:
                    self.speed = 1
                self.speedX += (self.dir[0] * (self.speed / 2)) # reduced speed
                self.speedY += (self.dir[1] * (self.speed / 2))
                self.speedX *= self.slowing_friction # increased friction
                self.speedY *= self.slowing_friction
                
            else: # if we need to go normal speed
                self.speedX += (self.dir[0] * self.speed) # calculate speed from direction to move and speed constant
                self.speedY += (self.dir[1] * self.speed)
                self.speedX *= self.normal_friction # apply friction
                self.speedY *= self.normal_friction

            self.trueX += self.speedX # store true x decimal values
            self.trueY += self.speedY
            self.rect.center = ( round(self.trueX), round(self.trueY) ) # apply values to sprite.center

 
    def get_node_color(self, level):
        """ returns rgb color constant based on level """
        color = medgray
        if level == 0:
            color = red
        elif level == 1:
            color = orange
        elif level == 2:
            color = yellow
        elif level == 3:
            color = green
        elif level == 4:
            color = blue        
        return color
            
 
