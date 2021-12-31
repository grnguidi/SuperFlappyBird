import pygame, sys, os
from os import environ
from sys import platform as sys_plat

from pygame.constants import DOUBLEBUF, HWSURFACE, RESIZABLE, VIDEORESIZE
from settings import *
from maps import *
from level import *


# enviroment settings
def platform():
    if 'ANDROID_ARGUMENT' in environ:
        return "android"
    elif sys_plat in ['linux', 'linux32', 'linux3']:
        return "linux"
    elif sys_plat in ['win32', 'cygwin']:
        return "win"

if platform()=="android":
    path="/data/data/org.game.supfb/files/app/"
elif platform()=="linux":
    path="./"

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

# game settings
clock = pygame.time.Clock()

game_scale = pygame.display.Info().current_h / screen_height #bug: screen scale issue

if platform() == "android":
    screen = pygame.display.set_mode((screen_width * game_scale, screen_height * game_scale), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((screen_width * game_scale * 0.9, screen_height * game_scale * 0.9), HWSURFACE|DOUBLEBUF)

pygame.display.set_caption("Super Flappy Bird")

font_big = pygame.font.Font('fonts/font.ttf', int(32))
font_medium = pygame.font.Font('fonts/font.ttf', int(24))
font_small = pygame.font.Font('fonts/font.ttf', int(16))


# screens

# initial menu
def main():

    menu_screen = pygame.Surface((screen_width, screen_height))
    menu_screen_scaled = pygame.Surface((screen.get_width(),screen.get_height()))

    title = font_big.render('Super Flappy Bird', True, 'green')
    title_rect = title.get_rect()
    title_rect.center = (screen_width / 2, screen_height / 2)

    text = font_medium.render('Press Space', True, 'green')
    text_rect = text.get_rect()
    text_rect.center = (screen_width / 2, title_rect.y + 70) 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]: #bug mouse button 2, 3 click
                    game()


        menu_screen.fill('navy')
        menu_screen.blit(title, title_rect)
        menu_screen.blit(text, text_rect)

        pygame.transform.scale(menu_screen, (screen.get_width(),screen.get_height()), menu_screen_scaled)

        screen.fill('black')
        screen.blit(menu_screen_scaled, (0,0))
        pygame.display.update()

        clock.tick(fps)


def credits():
    pass

# main game

def game():

    game_screen = pygame.Surface((screen_width, screen_height))
    game_screen_scaled = pygame.Surface((screen.get_width(),screen.get_height()))

    level = Level(level1_map, game_screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_m or event.key == pygame.K_ESCAPE:
                    main()

        game_screen.fill('cyan')
        level.run()

        pygame.transform.scale(game_screen, (screen.get_width(),screen.get_height()), game_screen_scaled)
        screen.fill('black')
        screen.blit(game_screen_scaled, (0,0))
        
        pygame.display.update()
        clock.tick(fps)
        if level.gameover == True:
            break
    
# game
while True:
    main()


