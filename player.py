from os import X_OK
import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        
        self.player_sprite = pygame.image.load(path+"imgs/flappybird.png").convert_alpha()
        self.image = self.player_sprite.copy() #pygame.Surface((player_size, player_size))
        self.rect = self.image.get_rect(topleft = pos)

        self.flap_sound = pygame.mixer.Sound("sounds/flap.wav")
        self.flap_sound.set_volume(0.5)
        self.hit_sound = pygame.mixer.Sound("sounds/hit.wav")
        self.hit_sound.set_volume(0.5) 
        self.drift_sound = pygame.mixer.Sound("sounds/drift.wav")
        self.drift_sound.set_volume(0.5)

        self.player_angle = 0
        self.direction = pygame.math.Vector2(1, 0)
        self.speed = 2
        self.gravity = 0.8
        self.flap = -10
        self.flap_possible = True
        self.play_drift = True 
        self.dead = False

    def get_direction(self):
        return self.direction

    def death_animation(self):
        self.speed = 0

    def update(self):    
        #check death
        if self.dead == False:
            #keys
            mousebutton = pygame.mouse.get_pressed()

            #flap
            if pygame.mouse.get_pressed()[0] == 1 and self.flap_possible == True and self.dead == False:
                self.flap_possible = False
                self.direction.y = self.flap
                self.flap_sound.play()
                self.play_drift = True
                if self.speed < 2:
                    self.speed += 0.5
                elif self.speed > 2:
                    self.speed = 2
                if self.player_angle < 25:
                    self.player_angle += 12
                    if self.speed < 2: # after drift
                        self.player_angle += 20

            if pygame.mouse.get_pressed()[0] == 0:
                self.flap_possible = True

            if self.rect.y < 50:
                self.flap_possible = False

            #moviment
            self.direction.y += self.gravity
            self.rect.y += self.direction.y          
            if self.player_angle > -25:
                self.player_angle -= 0.5
                if self.speed < 2: # during drift
                    self.player_angle -= 10 - self.speed 

        
        self.image = pygame.transform.rotate(self.player_sprite, self.player_angle)

