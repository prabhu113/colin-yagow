from block import *
import random

COLOR = (0, 255, 0)
SPEED = 4

class Good_Block(Block):
    width = 0
    height = 0
    screen_width = 0
    screen_height = 0
    
    def __init__(self, wid, hei, screen_wid, screen_hei,image):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        self.width = wid
        self.height = hei
        self.screen_width = screen_wid
        self.screen_height = screen_hei
        self.image = image
        # Call the parent class (Sprite) constructor
        super().__init__(COLOR, self.width, self.height, self.image)
        
    
            
    def update(self):
        def move(direction):
            if(direction == 0):
                self.rect.y -= SPEED
            elif(direction == 1):
                self.rect.x += SPEED
            elif(direction == 2):
                self.rect.y += SPEED
            elif(direction == 3):
                self.rect.x -= SPEED
        mov = random.randint(0, 4)
        if(mov == 0):
            if self.rect.y - SPEED >= 0: 
                move(0)
            else:
                move(2)
        elif(mov == 1):
            if self.rect.x + SPEED + self.width <= self.screen_width: 
                move(1)
            else:
                move(3)
        elif(mov == 2):
            if self.rect.y + SPEED + self.width <= self.screen_height: 
                move(2)
            else:
                move(0)
        elif(mov == 3):
            if self.rect.x >= 0: 
                move(3)
            else:
                move(1)
    
