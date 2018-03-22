
# Donovan Dobler, David Loegering, Colin Yagow

"""
Use sprites to collect blocks.
 
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
 
Explanation video: http://youtu.be/4W2AqUetBi4
"""
import pygame
import random
from block import *
from good_block import *
from bad_block import *
from files import *
from title_level import *
from player import *
from level_manager import *
from music_class import *
 
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
STARTING_BLOCK_NUMBER = 50

# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

 
# Initialize Pygame
pygame.init()

pygame.font.init()
SCORE_FONT = pygame.font.SysFont('Comic Sans MS', 40)
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
good_block_list = pygame.sprite.Group()
bad_block_list = pygame.sprite.Group()
 
# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
good_blocks_images = File('good_blocks.csv')
bad_blocks_images = File('bad_blocks.csv')
player_images = File('player.csv')

level_mgr = LevelManager()
music_file = File('music.csv')
music_dict = music_file.hashList()
music_mgr = Music(level_mgr, music_dict)

def StartGame(numb):
    global player
    global good_block_list
    good_block_list = pygame.sprite.Group()
    global bad_block_list
    bad_block_list = pygame.sprite.Group()
    global all_sprites_list
    all_sprites_list = pygame.sprite.Group()
    global score
    score = 0
    for i in range(numb):
        # This represents a block
        good_block_image_index = random.randint(0, 49)
        good_block_image = pygame.image.load(good_blocks_images.getData(good_block_image_index,1)).convert()
        good_block_image = pygame.transform.scale(good_block_image,(20,15))
        good_block_image.set_colorkey(BLACK)
        block = Good_Block(20, 15, screen_width, screen_height, good_block_image)
     
        # Set a random location for the block
        block.rect.x = random.randrange(screen_width-15)
        block.rect.y = random.randrange(screen_height-15)
     
        # Add the block to the list of objects
        good_block_list.add(block)
        all_sprites_list.add(block)

    for i in range(numb):
        # This represents a block
        bad_block_image = pygame.image.load(bad_blocks_images.getData(0,1)).convert()
        bad_block_image = pygame.transform.scale(bad_block_image,(20,15))
        bad_block_image.set_colorkey(BLACK)
        block = Bad_Block(20, 15, bad_block_image)
     
        # Set a random location for the block
        block.rect.x = random.randrange(screen_width-15)
        block.rect.y = random.randrange(screen_height-15)
     
        # Add the block to the list of objects
        bad_block_list.add(block)
        all_sprites_list.add(block)

    # Create a RED player block
    player_image = pygame.image.load(player_images.getData(0,1)).convert()
    player_image = pygame.transform.scale(player_image,(20,15))
    player_image.set_colorkey(BLACK)
    player = Player(screen_width, screen_height, player_image, music_mgr)
    all_sprites_list.add(player)

 
MENU = Main_Menu(screen, level_mgr, music_mgr)
level_mgr.load_level(MENU)

MENU.Open_Menu()
music_mgr.play_repeat()

StartGame(STARTING_BLOCK_NUMBER)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
player_speed_x = 4
player_speed_y = 4

# -------- Main Program Loop -----------
while not done:
    win = False
    if len(good_block_list) == 0:
        win = True
        player.setMovable(False)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.changespeed(0, -player_speed_x)
            if event.key == pygame.K_s:
                player.changespeed(0, player_speed_x)
            if event.key == pygame.K_d:
                player.changespeed(player_speed_y, 0)
            if event.key == pygame.K_a:
                player.changespeed(-player_speed_y, 0)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player.changespeed(0, player_speed_x)
            if event.key == pygame.K_s:
                player.changespeed(0, -player_speed_x)
            if event.key == pygame.K_d:
                player.changespeed(-player_speed_y, 0)
            if event.key == pygame.K_a:
                player.changespeed(player_speed_y, 0)
            if event.key == pygame.K_q:
                level_mgr.leave_level()
                MENU.Open_Menu()
                StartGame(50)
            if win:
                if event.key == pygame.K_y:
                    StartGame(STARTING_BLOCK_NUMBER)
                if event.key == pygame.K_n:
                    done = True
 
    # Clear the screen
    screen.fill(BLACK)
 
    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, good_block_list, True)
    # Check the list of collisions.

    good_blocks_images = File('good_blocks.csv')
    bad_blocks_images = File('bad_blocks.csv')
    for block in blocks_hit_list:
        good_block_list.remove(block)
        score += int(good_blocks_images.getData(0,2))
        music_mgr.play_once("good_block")
    blocks_hit_list = pygame.sprite.spritecollide(player, bad_block_list, True)
    # Check the list of collisions.
    for block in blocks_hit_list:
        if not win:
            score -= int(bad_blocks_images.getData(0,2))
            music_mgr.play_once("bad_block")
 
    # Draw all the spites
    player.update()
    good_block_list.update()
    bad_block_list.update()
    all_sprites_list.draw(screen)

    # Draw text
    textsurface = SCORE_FONT.render(str(score), False, WHITE)
    screen.blit(textsurface,(12,0))
    if win:
        textsurface = SCORE_FONT.render('Would You Like To Play Again (Y/N)', False, WHITE)
        text_rect = textsurface.get_rect(center=(screen_width/2, screen_height/2))
        screen.blit(textsurface,text_rect)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()
