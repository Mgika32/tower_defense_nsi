import pygame as pg
from turret_data import TURRET_DATA
import math

class Turret(pg.sprite.Sprite):
    def __init__(self, sprite_sheets, tile_x, tile_y):
        pg.sprite.Sprite.__init__(self)
        self.upgrade_level = 1
        self.range = TURRET_DATA[self.upgrade_level - 1].get("range")
        self.cooldown = TURRET_DATA[self.upgrade_level - 1].get("cooldown")
        self.last_shot = pg.time.get_ticks()
        self.selected = False
        self.target = None
    
        #position variables
        self.tile_x = tile_x
        self.tile_y = tile_y
        #calculate center coordinates
        self.x = (self.tile_x + 0.5) * 48
        self.y = (self.tile_y + 0.5) * 48

    def pick_target(self, enemy_group):
        x_dist = 0
        y_dist = 0
    #check distance to each enemy to see if it is in range
        for enemy in enemy_group:
          if enemy.health > 0:
            x_dist = enemy.pos[0] - self.x
            y_dist = enemy.pos[1] - self.y
            dist = math.sqrt(x_dist ** 2 + y_dist ** 2)
            if dist < self.range:
              self.target = enemy
              self.angle = math.degrees(math.atan2(-y_dist, x_dist))
              #damage enemy
              self.target.health -= 5
              break

