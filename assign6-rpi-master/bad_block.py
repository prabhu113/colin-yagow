from block import *
import pygame
import random
import math

COLOR = (255, 0, 0)

class Bad_Block(Block):
    def __init__(self, width, height, image):
        self.image = image
        super().__init__(COLOR, width, height, self.image)
        
        # The "center" of the orbit
        self.center_x = random.randrange(700)
        self.center_y = random.randrange(400)
 
        # Where along the orbit the object is at
        self.angle = random.random() * 2 * math.pi
 
        # Radius of the orbit
        self.radius = random.randrange(10, 200)
 
        # Speed of orbit
        self.speed = .01

    def update(self):
        self.rect.x = self.radius * math.sin(self.angle) + self.center_x
        self.rect.y = self.radius * math.cos(self.angle) + self.center_y
 
        self.angle += self.speed
