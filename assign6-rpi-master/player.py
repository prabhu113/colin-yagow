import pygame
class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    movable = True
    # -- Methods
    def __init__(self, x, y, image, music_mgr):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        self.image = image
        self.music_mgr = music_mgr

        # Set height, width
        #self.image = pygame.Surface([15, 15])
        #self.image.fill((0,0,255))
 
        # Make our middle the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x/2
        self.rect.y = y/2

        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0

        self.screen_width = x
        self.screen_height = y
 
    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y

    def setMovable(self, move):
        self.movable = move
 
    def update(self):
        """ Find a new position for the player"""
        if self.movable:
            if (self.rect.x + self.change_x >= 0 and self.rect.x + self.change_x <= self.screen_width - 15):
                self.rect.x += self.change_x
            else:
                self.music_mgr.play_once("border")
            if (self.rect.y + self.change_y >= 0 and self.rect.y + self.change_y <= self.screen_height - 15):
                self.rect.y += self.change_y
            else:
                self.music_mgr.play_once("border")
                
