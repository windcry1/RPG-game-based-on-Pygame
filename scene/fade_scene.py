import os
import enum
import pygame
import sys
from pygame.locals import *


class SceneStatus(enum.IntEnum):
    In = 1
    Normal = 2
    Out = 3


class FadeScene:
    def __init__(self, back_image: pygame.image):
        self.back_image = back_image
        self.alpha = 0
        self.status = SceneStatus.In

    def set_status(self, status: SceneStatus):
        self.status = status
        if status == SceneStatus.In:
            self.alpha = 0  # 透明
        if status == SceneStatus.Normal:
            self.alpha = 255  # 不透明
        if status == SceneStatus.Out:
            self.alpha = 0  # 透明

    def get_back_image(self, win_posx: int, win_posy: int):
        if win_posx < 0:
            win_posx = 0
        if win_posy < 0:
            win_posy = 0
        if win_posx > self.back_image.get_width() - 800:
            win_posx = self.back_image.get_width() - 800
        if win_posy > self.back_image.get_height() - 600:
            win_posy = self.back_image.get_height() - 600
        temp_surface = self.back_image.subsurface((win_posx, win_posy, 800, 600))
        if self.status == SceneStatus.Normal:
            return temp_surface
        elif self.status == SceneStatus.In:
            temp_surface.set_alpha(self.alpha)
            black_surface = pygame.Surface((800, 600))
            black_surface.blit(temp_surface, (0, 0))
            self.alpha += 10
            if self.alpha >= 255:
                self.alpha = 0
                self.status = SceneStatus.Normal
            return black_surface
        elif self.status == SceneStatus.Out:
            temp_surface.set_alpha(255 - self.alpha)
            black_surface = pygame.Surface((800, 600))
            black_surface.blit(temp_surface, (0, 0))
            self.alpha += 10
            if self.alpha >= 255:
                self.alpha = 255
            return black_surface

    def get_out(self):
        if self.status == SceneStatus.Out and self.alpha == 255:
            return True
        else:
            return False
