import pygame
from settings import *
from tiles import Tile
from player import Player
from maps import *
from nest import Nest

class Level():
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.gameover = False

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.nests = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == "O":
                    tile = Tile((x, y), tile_size)
                    tile.image.fill('brown')
                    self.tiles.add(tile)
        
                if cell == "X":
                    tile = Tile((x, y), tile_size)
                    tile.image.fill('green')
                    tile.friction = 0.03
                    self.tiles.add(tile)

                if cell == "P":
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)

                if cell in ["1","2","3","4","5","6","7","8","9","0"]:
                    nest = Nest((x, y), tile_size)
                    nest.image.fill('black')
                    nest.level = cell
                    self.nests.add(nest)


    def run(self):
        #backgrounds

        #player
        self.player.update()
        player = self.player.sprite
        player_x = player.speed
        direction_x = player.direction.x * -1

        #check collision
        for sprite in self.tiles:
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    #slide
                    if player.speed > 1 and player.direction.y <= 15:
                        player.speed -= sprite.friction
                        player.rect.bottom = sprite.rect.top
                        player.direction.y = 0
                        if player.play_drift:
                            player.drift_sound.play()
                            player.play_drift = False
                    else:
                        player.speed = 0
                        player.player_angle = -90
                        player.dead = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.dead = True
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.dead = True
        if player.rect.y > screen_height - 40:
            player.speed = 0
            player.dead = True

        #check level change            
        for sprite in self.nests.sprites():
            if player.rect.colliderect(sprite.rect):
                level_map = level1_map
                if (sprite.level == "2"):
                   level_map = level2_map
                elif (sprite.level == "3"):
                   level_map = level3_map
                
                self.__init__(level_map,self.display_surface)

        #check death
        if player.dead == True:
            player.drift_sound.stop()
            player.hit_sound.play()
            player_x = 0
            direction_x = 0
            pygame.time.wait(1500)
            self.gameover = True 

        #check nest

        #camera correction
        camera_speed = player_x * direction_x

        if player.rect.x > screen_width / 4:
            player.rect.x -= player.speed


        #tiles
        self.tiles.update(camera_speed)
        self.nests.update(camera_speed)

        #update screen
        #to do:background draw
        self.tiles.draw(self.display_surface)
        self.nests.draw(self.display_surface)
        self.player.draw(self.display_surface)





