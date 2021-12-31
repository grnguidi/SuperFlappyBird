import pygame

class Nest(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size / 2))
        self.image.fill('black')
        self.rect = self.image.get_rect(topleft = pos)
        self.level = 1

    def update(self, x_shift):
        self.rect.x += x_shift