#Need level mananger to identify what level we are on
from level_manager import *
import pygame
from title_level import *
from credits_level import *


class Music():           
    def __init__(self, level_mgr, music_dict):
        self.level_mgr = level_mgr
        self.music_dict = music_dict
        pygame.init()
        pygame.mixer.init()
    def what_song(self):
        if isinstance(self.level_mgr.get_current_level(), Main_Menu):
            return self.music_dict["title"]
        elif isinstance(self.level_mgr.get_current_level(), Credits_Level):
            return self.music_dict["credits"]
        else:
            return self.music_dict["level"]
        
        
    def play_once(self, sound):
        sound = pygame.mixer.Sound(self.music_dict[sound])
        sound.play()
    def play_repeat(self):
        pygame.mixer.music.stop()
        print(self.what_song())
        pygame.mixer.music.load(self.what_song())
        pygame.mixer.music.play(-1)
    def stop_repeat(self):
        pygame.mixer.music.stop()
