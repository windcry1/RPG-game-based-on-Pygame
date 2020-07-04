"""
# >>> Author: WindCry1
# >>> Mail: lanceyu120@gmail.com
# >>> Website: https://windcry1.com
# >>> Date: 2020/7/3 10:22
"""
import os
import pygame
from pygame.locals import *
from tiled_scene import TileScene as tilescene
from scene.fade_scene import FadeScene, SceneStatus
from actor.player import Player
from actor.monster2 import Monster
from actor.items import Sword1, Sword2, Sword3, Cloud
from scene import SceneResult
import pytmx


class Scene2:
    def __init__(self, player: Player, surface: pygame.Surface):
        self.scene_result = SceneResult.Ongoing
        self.screen = surface
        back_tmx_path = os.path.join('resources', 'tmx', 'scene2.tmx')
        player_music_path = os.path.join('resources', 'bgm', 'swk.wav')
        self.player_music = pygame.mixer.Sound(player_music_path)
        monster_music_path = os.path.join('resources', 'bgm', 'monster.wav')
        self.monster_music = pygame.mixer.Sound(monster_music_path)
        music_path = os.path.join('resources', 'bgm', 'temple.wav')
        pygame.mixer.init()
        pygame.mixer_music.load(music_path)
        pygame.mixer.music.play(-1, 0)
        self.tiled_scene = tilescene(back_tmx_path)
        self.back_surface = self.tiled_scene.surface
        self.fade_scene = FadeScene(self.back_surface)
        self.temp_surface = pygame.Surface((800, 600))
        self.player = player
        self.cloud = None
        self.monster = None
        self.sword1 = None
        self.sword2 = None
        self.sword3 = None
        self.start_time = pygame.time.get_ticks()
        self.now = 0
        self.obstacle_group = pygame.sprite.Group()
        self.dx_dy = [0, 0]
        self.win_pos_x = 0
        self.win_pos_y = 0
        self.treasure = pygame.sprite.Group()
        self.init_actor()

    def init_actor(self):
        for group in self.tiled_scene.tiled.tmx_data.objectgroups:
            if isinstance(group, pytmx.pytmx.TiledObjectGroup):
                if group.name == 'actor':
                    for obj in group:
                        if obj.name == 'player':
                            self.player.set_pos(obj.x, obj.y)
                            self.win_pos_x = obj.x - 400
                            self.win_pos_y = obj.y - 300
                        if obj.name == 'sword1':
                            self.sword1 = Sword1(obj.x, obj.y)
                        if obj.name == 'sword2':
                            self.sword2 = Sword2(obj.x, obj.y)
                        if obj.name == 'monster':
                            self.monster = Monster(obj.x, obj.y)
                        if obj.name == 'cloud':
                            self.cloud = Cloud(obj.x, obj.y, obj.width, obj.height)
                if group.name == 'obstacle':
                    for obj in group:
                        obs = pygame.sprite.Sprite()
                        obs.rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                        self.obstacle_group.add(obs)

    def get_current_surface(self):
        win_surface = self.fade_scene.get_back_image(self.win_pos_x, self.win_pos_y)
        self.temp_surface.blit(win_surface, (0, 0))
        self.player.draw(self.temp_surface, self.win_pos_x, self.win_pos_y)
        self.monster.draw(self.temp_surface, self.win_pos_x, self.win_pos_y)
        self.sword1.draw(self.temp_surface, self.win_pos_x, self.win_pos_y)
        self.sword2.draw(self.temp_surface, self.win_pos_x, self.win_pos_y)
        if self.sword3:
            self.sword3.draw(self.temp_surface, self.win_pos_x, self.win_pos_y)
        self.cloud.draw(self.temp_surface, 200, 250)
        self.screen.blit(self.temp_surface, (0, 0))

    def run(self):
        clock = pygame.time.Clock()
        scene_exit = False
        tick = 1000
        move_char = 0
        while not scene_exit:
            self.dx_dy = [0, 0]
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.fade_scene.set_status(SceneStatus.Out)
                    self.scene_result = SceneResult.Quit
                if event.type == KEYDOWN and not self.player.is_stop:
                    key_down = True
                    if self.sword1.crashed and not self.sword1.get:
                        self.player.attack += 10
                        self.sword1.get = True
                    if self.sword2.crashed and not self.sword2.get:
                        self.player.attack += 10
                        self.sword2.get = True
                    if self.sword3 and self.sword3.crashed and not self.sword3.get:
                        self.player.attack += 960
                        self.sword3.get = True
                    if self.cloud.crashed and self.scene_result != SceneResult.Quit:
                        self.fade_scene.set_status(SceneStatus.Out)
                        self.scene_result = SceneResult.Quit
                    if self.monster.crashed:
                        self.monster.get = True
                        self.player.is_stop = True
                        self.now = self.start_time // tick
                        self.start_time = pygame.time.get_ticks()
                    pressed_key = event.key
                    self.dx_dy = self.player.key_move(pressed_key, key_down, self.obstacle_group)
                    if key_down:
                        self.win_pos_x += self.dx_dy[0]
                        self.win_pos_y += self.dx_dy[1]
            if self.fade_scene.get_out():
                scene_exit = True
            if self.win_pos_x < 0:
                self.win_pos_x = 0
            if self.win_pos_y < 0:
                self.win_pos_y = 0
            if self.win_pos_x > 8000 - 800:
                self.win_pos_x = 8000 - 800
            if self.win_pos_y > 6240 - 600:
                self.win_pos_y = 6240 - 600
            if self.fade_scene.status != SceneStatus.Out:
                self.cloud.collide(self.player)
                if self.cloud.crashed:
                    if self.player.skill:
                        self.cloud.crashed = False
                self.monster.collide(self.player)
                if not self.sword1.get:
                    self.sword1.collide(self.player)
                if not self.sword2.get:
                    self.sword2.collide(self.player)
                if self.sword1.get and self.sword2.get and not self.sword3:
                    self.sword3 = Sword3(self.player.pos_x, self.player.pos_y)
                    self.sword3.crashed = True
                if self.player.is_stop:
                    if self.monster.hp <= 0:
                        self.monster.hp = 0
                        self.scene_result = SceneResult.Win
                        self.player.is_stop = False
                        self.fade_scene.status = SceneStatus.Out
                    if self.player.hp <= 0:
                        self.player.hp = 0
                        self.scene_result = SceneResult.Fail
                        self.fade_scene.status = SceneStatus.Out
                    else:
                        time = pygame.time.get_ticks()
                        if time//tick != self.now:
                            self.now = time//tick
                            if move_char == 0:
                                self.monster.hp -= self.player.attack
                                move_char = 1
                                self.player_music.play()
                            else:
                                self.player.hp -= self.monster.attack
                                move_char = 0
                                self.monster_music.play()
            self.get_current_surface()
            pygame.display.update()
            clock.tick(15)
        pygame.mixer_music.stop()

