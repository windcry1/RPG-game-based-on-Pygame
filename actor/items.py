"""
# >>> Author: WindCry1
# >>> Mail: lanceyu120@gmail.com
# >>> Website: https://windcry1.com
# >>> Date: 2020/7/3 15:53
"""
import pygame
import actor
from dialog.dialog import Dialog


class Sword0(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.walk_frames = actor.DirAction('sword0', '', '', 1, 1, True)
        self.width = 64
        self.height = 64
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        self.crashed = False
        self.get = False
        self.dialog = Dialog(400, 130, '成功获得了武器净蚀 攻击力提升10 按任意键继续')

    def draw(self, surface: pygame.Surface, win_x, win_y):
        if not self.get:
            current_frame = self.walk_frames.get_curr_frame(0)
            surface.blit(current_frame, (self.pos_x - win_x, self.pos_y - win_y))
            if self.crashed:
                surface.blit(self.dialog.surface, (self.pos_x - win_x - 200, self.pos_y - win_y - 150))

    def set_pos(self, init_pos_x, init_pos_y):
        self.pos_x = init_pos_x
        self.pos_y = init_pos_y

    def collide(self, sprite):
        if pygame.sprite.collide_rect(sprite, self):
            self.crashed = True
        else:
            self.crashed = False


class Sword1(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.walk_frames = actor.DirAction('sword1', '', '', 1, 1, True)
        self.width = 64
        self.height = 64
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        self.crashed = False
        self.get = False
        self.dialog = Dialog(400, 130, '成功获得了武器耀光 攻击力提升10 按任意键继续')

    def draw(self, surface: pygame.Surface, win_x, win_y):
        if not self.get:
            current_frame = self.walk_frames.get_curr_frame(0)
            surface.blit(current_frame, (self.pos_x - win_x, self.pos_y - win_y))
            if self.crashed:
                surface.blit(self.dialog.surface, (self.pos_x - win_x, self.pos_y - win_y - 150))

    def set_pos(self, init_pos_x, init_pos_y):
        self.pos_x = init_pos_x
        self.pos_y = init_pos_y

    def collide(self, sprite):
        if pygame.sprite.collide_rect(sprite, self):
            self.crashed = True
        else:
            self.crashed = False


class Sword2(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.walk_frames = actor.DirAction('sword2', '', '', 1, 1, True)
        self.width = 64
        self.height = 64
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        self.crashed = False
        self.get = False
        self.dialog = Dialog(400, 130, '成功获得了武器蜂刺 攻击力提升10 按任意键继续')

    def draw(self, surface: pygame.Surface, win_x, win_y):
        if not self.get:
            current_frame = self.walk_frames.get_curr_frame(0)
            surface.blit(current_frame, (self.pos_x - win_x, self.pos_y - win_y))
            if self.crashed:
                surface.blit(self.dialog.surface, (self.pos_x - win_x, self.pos_y - win_y - 150))

    def set_pos(self, init_pos_x, init_pos_y):
        self.pos_x = init_pos_x
        self.pos_y = init_pos_y

    def collide(self, sprite):
        if pygame.sprite.collide_rect(sprite, self):
            self.crashed = True
        else:
            self.crashed = False


class Sword3(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.walk_frames = actor.DirAction('sword3', '', '', 1, 1, True)
        self.width = 64
        self.height = 64
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        self.crashed = False
        self.get = False
        self.dialog = Dialog(400, 190, '恭喜你成功集齐三把神器 合成获得神器三相之力 获得了神一般的力量 按任意键继续')

    def draw(self, surface: pygame.Surface, win_x, win_y):
        if not self.get:
            current_frame = self.walk_frames.get_curr_frame(0)
            surface.blit(current_frame, (self.pos_x - win_x, self.pos_y - win_y))
            if self.crashed:
                surface.blit(self.dialog.surface, (self.pos_x - win_x, self.pos_y - win_y - 150))

    def set_pos(self, init_pos_x, init_pos_y):
        self.pos_x = init_pos_x
        self.pos_y = init_pos_y

    def collide(self, sprite):
        if pygame.sprite.collide_rect(sprite, self):
            self.crashed = True
        else:
            self.crashed = False


class Shield(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.walk_frames = actor.DirAction('shield', '', '', 1, 1, True)
        self.width = 64
        self.height = 64
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        self.crashed = False
        self.get = False
        self.dialog = Dialog(400, 130, '成功获得了武器木盾 血量提升五十点 按任意键继续')

    def draw(self, surface: pygame.Surface, win_x, win_y):
        if not self.get:
            current_frame = self.walk_frames.get_curr_frame(0)
            surface.blit(current_frame, (self.pos_x - win_x, self.pos_y - win_y))
            if self.crashed:
                surface.blit(self.dialog.surface, (self.pos_x - win_x - 200, self.pos_y - win_y - 150))

    def set_pos(self, init_pos_x, init_pos_y):
        self.pos_x = init_pos_x
        self.pos_y = init_pos_y

    def collide(self, sprite):
        if pygame.sprite.collide_rect(sprite, self):
            self.crashed = True
        else:
            self.crashed = False


class Cloud(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        self.crashed = False
        self.dialog = Dialog(400, 130, '你并不会腾云驾雾技能 不能再往前面走了 按任意键继续')

    def draw(self, surface: pygame.Surface, win_x, win_y):
        if self.crashed:
            surface.blit(self.dialog.surface, (win_x, win_y))

    def collide(self, sprite):
        if pygame.sprite.collide_rect(sprite, self):
            self.crashed = True
        else:
            self.crashed = False
