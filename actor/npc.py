"""
# >>> Author: WindCry1
# >>> Mail: lanceyu120@gmail.com
# >>> Website: https://windcry1.com
# >>> Date: 2020/7/3 13:33
"""
import pygame
import actor
from dialog.dialog import Dialog


class NPC(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.walk_frames = actor.DirAction('NPC', '', '', 1, 4, True)
        self.dir = 0
        self.step_count = 0
        self.width = 32
        self.height = 48
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        self.crashed = False
        self.get = False
        self.dialog = Dialog(400, 190, '你好勇士 我是这里的仙人 被魔界人追杀到这里 功力全失 我依稀还记得腾云驾雾 你是否要学习呢 (按Y键学习腾云驾雾)', True)
        self.dialog_get = Dialog(400, 70, '你已经学习了腾云驾雾')

    def draw(self, surface: pygame.Surface, win_x, win_y):
        current_frame = self.walk_frames.get_curr_frame(self.dir)
        surface.blit(current_frame, (self.pos_x - win_x, self.pos_y - win_y))
        if self.crashed:
            if self.get:
                surface.blit(self.dialog_get.surface, (self.pos_x - win_x, self.pos_y - win_y - 150))
            else:
                surface.blit(self.dialog.surface, (self.pos_x - win_x, self.pos_y - win_y - 150))

    def set_pos(self, init_pos_x, init_pos_y):
        self.pos_x = init_pos_x
        self.pos_y = init_pos_y

    def collide(self, sprite):
        if pygame.sprite.collide_rect(sprite, self):
            self.crashed = True
        else:
            self.crashed = False
