"""
# >>> Author: WindCry1
# >>> Mail: lanceyu120@gmail.com
# >>> Website: https://windcry1.com
# >>> Date: 2020/7/3 10:38
"""
import os
import pygame
from scene.fade_scene import FadeScene, SceneStatus
from scene import SceneResult
from pygame.locals import *


class Scene0:
    def __init__(self, surface: pygame.Surface):
        self.screen = surface
        self.win_pos_x = 0
        self.win_pos_y = 0
        self.scene_result = SceneResult.Ongoing
        self.image_path = os.path.join('resources', 'img', 'scene0.png')
        self.scene = pygame.image.load(self.image_path)
        self.fade_scene = FadeScene(self.scene)
        self.temp_surface = pygame.Surface((800, 600))

    def run(self):
        clock = pygame.time.Clock()
        scene_exit = False
        is_end = False
        start_time = pygame.time.get_ticks()
        while not scene_exit:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.scene_result = SceneResult.Quit
                    scene_exit = True
            self.get_current_surface()
            pygame.display.update()
            time = pygame.time.get_ticks()
            if self.fade_scene.get_out():
                self.scene_result = SceneResult.Next
                scene_exit = True
            if time - start_time >= 5000 and not is_end:
                self.fade_scene.set_status(SceneStatus.Out)
                is_end = True

            clock.tick(30)

    def get_current_surface(self):
        win_surface = self.fade_scene.get_back_image(self.win_pos_x, self.win_pos_y)
        self.temp_surface.blit(win_surface, (0, 0))
        self.screen.blit(self.temp_surface, (0, 0))
