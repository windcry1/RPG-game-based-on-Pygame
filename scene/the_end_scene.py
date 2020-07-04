"""
# >>> Author: WindCry1
# >>> Mail: lanceyu120@gmail.com
# >>> Website: https://windcry1.com
# >>> Date: 2020/7/3 10:22
"""
import os
import pygame
from pygame.locals import *
from scene import SceneResult
from scene.fade_scene import FadeScene, SceneStatus


class TheEndScene:
    def __init__(self, state, surface: pygame.Surface):
        self.screen = surface
        self.win_pos_x = 0
        self.win_pos_y = 0
        win_img_path = os.path.join('resources', 'img', 'win.png')
        fail_img_path = os.path.join('resources', 'img', 'fail.png')
        if state:
            self.image = pygame.image.load(win_img_path)
        else:
            self.image = pygame.image.load(fail_img_path)
        self.fade_scene = FadeScene(self.image)
        self.temp_surface = pygame.Surface((800, 600))

    def run(self):
        clock = pygame.time.Clock()
        exit = False
        is_end = False
        start_time = pygame.time.get_ticks()
        while not exit:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit = True
            self.get_current_surface()
            pygame.display.update()
            time = pygame.time.get_ticks()
            if self.fade_scene.get_out():
                exit = True
            if time - start_time >= 5000 and not is_end:
                self.fade_scene.set_status(SceneStatus.Out)
                is_end = True
            clock.tick(30)

    def get_current_surface(self):
        win_surface = self.fade_scene.get_back_image(self.win_pos_x, self.win_pos_y)
        self.temp_surface.blit(win_surface, (0, 0))
        self.screen.blit(self.temp_surface, (0, 0))
