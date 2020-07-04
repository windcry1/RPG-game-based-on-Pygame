"""
# >>> Author: WindCry1
# >>> Mail: lanceyu120@gmail.com
# >>> Website: https://windcry1.com
# >>> Date: 2020/7/3 10:28
"""
import os
import pygame
import actor
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        font_path = os.path.join('resources', 'font', 'msyh.ttf')
        self.font = pygame.font.Font(font_path, 18)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.walk_frames = actor.DirAction('player', '', '', 4, 4, True)
        self.dir = 0
        self.hp = 100
        self.max_hp = 100
        self.attack = 10
        self.width = 32
        self.height = 48
        self.skill = False
        self.is_stop = False
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)

    def draw(self, surface: pygame.Surface, win_x, win_y):
        current_frame = self.walk_frames.get_curr_frame(self.dir)
        surface.blit(current_frame, (self.pos_x - win_x, self.pos_y - win_y))
        pygame.draw.rect(surface, (0, 0, 255),
                         pygame.Rect(self.pos_x - win_x + 16 - self.max_hp // 4 - 2, self.pos_y - win_y - 17, self.max_hp//2 + 4, 14))
        pygame.draw.rect(surface, (255, 0, 0),
                         pygame.Rect(self.pos_x - win_x + 16 - self.max_hp // 4, self.pos_y - win_y - 15, self.hp//2, 10))
        surface.blit(self.font.render('当前攻击力：' + '%d' % self.attack, 0, (255, 0, 0)), (20, 20))

    def set_pos(self, init_pos_x, init_pos_y):
        self.pos_x = init_pos_x
        self.pos_y = init_pos_y

    def key_move(self, pressed_key: int, key_click: bool, obstacle_group: pygame.sprite.Group):
        if not key_click or self.is_stop:
            return [0, 0]
        pos_x = self.pos_x
        pos_y = self.pos_y
        if pressed_key == K_UP:
            self.dir = 3
            pos_y -= 32
        elif pressed_key == K_DOWN:
            self.dir = 0
            pos_y += 32
        elif pressed_key == K_LEFT:
            self.dir = 1
            pos_x -= 32
        elif pressed_key == K_RIGHT:
            self.dir = 2
            pos_x += 32
        else:
            return [0, 0]
        self.rect = pygame.Rect(pos_x, pos_y, self.width, self.height)
        collide_list = pygame.sprite.spritecollide(self, obstacle_group, False)
        if collide_list:
            return [0, 0]
        else:
            return self.move()

    def move(self):
        x = 0
        y = 0
        if self.dir == 3:
            y = -32
        elif self.dir == 0:
            y = 32
        elif self.dir == 1:
            x = -32
        elif self.dir == 2:
            x = 32
        self.pos_x += x
        self.pos_y += y
        return [x, y]
