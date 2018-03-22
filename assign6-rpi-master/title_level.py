import pygame
from credits_level import *
from dummy_object import *
from level_manager import *

class Main_Menu():
    def __init__(self, _screen, level_mgr, music_mgr):
        self.screen = _screen
        pygame.font.init()
        self.TITLE_FONT = pygame.font.SysFont('Comic Sans MS', 60)
        self.OPTIONS_FONT = pygame.font.SysFont('Comic Sans MS', 20)
        self.level_mgr = level_mgr
        self.music_mgr = music_mgr
        super().__init__()

    def Open_Menu(self):

        visable = True
        menu = 0  #0 = main menu 1 = how_to_play 2 = credits
        self.music_mgr.play_repeat()
        while visable:
            self.screen.fill((0,0,0))
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_q:
                        menu = 0
                        self.music_mgr.play_repeat()
                    if event.key == pygame.K_w:
                        menu = 1
                        self.music_mgr.play_repeat()
                    if event.key == pygame.K_e:
                        menu = 2
                        self.music_mgr.play_repeat()
                    if event.key == pygame.K_x:
                        menu = 3
                    if event.key == pygame.K_SPACE:
                        game_object = Dummy('game')
                        self.level_mgr.load_level(game_object)
                        self.music_mgr.play_repeat()
                        visable = False
            if menu == 0:
                textsurface = self.TITLE_FONT.render('SPACE ADVENTURE', False, (255, 0, 0))
                self.screen.blit(textsurface,(0,0))
                textsurface = self.OPTIONS_FONT.render('Press Space to Begin', False, (255, 0, 0))
                self.screen.blit(textsurface,(3,65))
                textsurface = self.OPTIONS_FONT.render('Press w for How to Play', False, (255, 0, 0))
                self.screen.blit(textsurface,(3,90))
                textsurface = self.OPTIONS_FONT.render('Press e for Credits', False, (255, 0, 0))
                self.screen.blit(textsurface,(3,115))
                textsurface = self.OPTIONS_FONT.render('Press x to close game', False, (255, 0, 0))
                self.screen.blit(textsurface,(3,140))
            if menu == 1:
                textsurface = self.OPTIONS_FONT.render('Use w, s, a, and d to move your astronaut and collect space ship parts.', False, (255, 0, 0))
                self.screen.blit(textsurface,(3,30))
                textsurface = self.OPTIONS_FONT.render('Be sure to avoid the asteroids!', False, (255, 0, 0))
                self.screen.blit(textsurface,(3,55))
                textsurface = self.OPTIONS_FONT.render('Press the q key at any time to go to the main menu.', False, (255, 0, 0))
                self.screen.blit(textsurface,(3,105))
            if menu == 2:
                credit = Credits_Level(self.screen, self.level_mgr, self.music_mgr)
                self.level_mgr.load_level(credit)
                credit.Open_Credits()
                menu = 0
                self.music_mgr.play_repeat()
            if menu == 3:
                pygame.quit()
                
            pygame.display.flip()
