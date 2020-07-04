"""
# >>> Author: WindCry1
# >>> Mail: lanceyu120@gmail.com
# >>> Website: https://windcry1.com
# >>> Date: 2020/7/3 10:31
"""

import pygame
import actor
from dialog.dialog import Dialog


class Monster(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.walk_frames = actor.DirAction('monster2', '', '', 1, 4, True)
        self.width = 312 * 2
        self.height = 310 * 2
        self.hp = 1000
        self.max_hp = 1000
        self.attack = 150
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        self.crashed = False
        self.get = False
        self.dialog = Dialog(240, 180, '遇到怪物 开始战斗 按任意键继续')

    def draw(self, surface: pygame.Surface, win_x, win_y):
        current_frame = self.walk_frames.get_curr_frame(0)
        surface.blit(current_frame, (self.pos_x - win_x, self.pos_y - win_y))
        pygame.draw.rect(surface, (0, 0, 255),
                         pygame.Rect(self.pos_x - win_x - self.max_hp // 4 - 2, self.pos_y - win_y - 17,
                                     self.max_hp // 2 + 4, 14))
        pygame.draw.rect(surface, (255, 0, 0),
                         pygame.Rect(self.pos_x - win_x - self.max_hp // 4, self.pos_y - win_y - 15, self.hp // 2, 10))
        if not self.get:
            if self.crashed:
                surface.blit(self.dialog.surface, (self.pos_x - win_x, self.pos_y - win_y + 200))

    def set_pos(self, init_pos_x, init_pos_y):
        self.pos_x = init_pos_x
        self.pos_y = init_pos_y

    def collide(self, sprite):
        if pygame.sprite.collide_rect(sprite, self):
            self.crashed = True
        else:
            self.crashed = False
