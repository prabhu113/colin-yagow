import pygame
from files import *
from level_manager import *


class Credits_Level():
    def __init__(self, _screen, level_mgr, music_mgr):
        self.screen = _screen
        self.level_mgr = level_mgr
        self.music_mgr = music_mgr
        pygame.font.init()
        self.TITLE_FONT_SIZE = 60
        self.TITLE_FONT = pygame.font.SysFont('Comic Sans MS', self.TITLE_FONT_SIZE)
        self.CREDITS_FONT_SIZE = 15
        self.CREDITS_FONT = pygame.font.SysFont('Comic Sans MS', self.CREDITS_FONT_SIZE)
        super().__init__()

    def Open_Credits(self):
        visable = True
        self.music_mgr.play_repeat()
        while visable:
            self.screen.fill((0,0,0))
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_q:
                        self.level_mgr.leave_level()
                        visable = False

            credits_file = File('credits.csv')
            credits_list = credits_file.getAll()
            
            textsurface = self.TITLE_FONT.render('Credits', False, (255, 0, 0))
            self.screen.blit(textsurface,(0,0))
            count = 0
            for list in credits_list:
                textsurface = self.CREDITS_FONT.render(list[0], False, (255, 0, 0))
                self.screen.blit(textsurface,(3, self.TITLE_FONT_SIZE + (count * (self.CREDITS_FONT_SIZE + 4)) +18))
                count += 1

            textsurface = self.CREDITS_FONT.render('Press the q key to return to the main menu', False, (255, 0, 0))
            self.screen.blit(textsurface,(3, self.TITLE_FONT_SIZE + ((count + 1) * (self.CREDITS_FONT_SIZE + 4)) +18))
            
            pygame.display.flip()


