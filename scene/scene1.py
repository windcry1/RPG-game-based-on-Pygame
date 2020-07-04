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
from actor.monster1 import Monster
from actor.npc import NPC
from actor.items import Sword0, Shield
from scene import SceneResult
import pytmx


class Scene1:
    def __init__(self, surface: pygame.Surface):
        self.scene_result = SceneResult.Ongoing
        self.screen = surface
        back_tmx_path = os.path.join('resources', 'tmx', 'scene1.tmx')
        player_music_path = os.path.join('resources', 'bgm', 'swk.wav')
        self.player_music = pygame.mixer.Sound(player_music_path)
        monster_music_path = os.path.join('resources', 'bgm', 'monster.wav')
        music_path = os.path.join('resources', 'bgm', 'village.wav')
        pygame.mixer.init()
        pygame.mixer_music.load(music_path)
        pygame.mixer.music.play(-1, 0)
        self.monster_music = pygame.mixer.Sound(monster_music_path)
        self.tiled_scene = tilescene(back_tmx_path)
        self.back_surface = self.tiled_scene.surface
        self.fade_scene = FadeScene(self.back_surface)
        self.temp_surface = pygame.Surface((800, 600))
        self.player = None
        self.npc = None
        self.monster = None
        self.sword = None
        self.shield = None
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
                            self.player = Player(obj.x, obj.y)
                            self.win_pos_x = obj.x - 400
                            self.win_pos_y = obj.y - 300
                        if obj.name == 'npc':
                            self.npc = NPC(obj.x, obj.y)
                        if obj.name == 'sword':
                            self.sword = Sword0(obj.x, obj.y)
                        if obj.name == 'shield':
                            self.shield = Shield(obj.x, obj.y)
                        if obj.name == 'monster':
                            self.monster = Monster(obj.x, obj.y)
                if group.name == 'obstacle':
                    for obj in group:
                        obs = pygame.sprite.Sprite()
                        obs.rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                        self.obstacle_group.add(obs)

    def get_current_surface(self):
        win_surface = self.fade_scene.get_back_image(self.win_pos_x, self.win_pos_y)
        self.temp_surface.blit(win_surface, (0, 0))
        self.player.draw(self.temp_surface, self.win_pos_x, self.win_pos_y)
        self.npc.draw(self.temp_surface, self.win_pos_x, self.win_pos_y)
        self.monster.draw(self.temp_surface, self.win_pos_x, self.win_pos_y)
        self.sword.draw(self.temp_surface, self.win_pos_x, self.win_pos_y)
        self.shield.draw(self.temp_surface, self.win_pos_x, self.win_pos_y)
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
                    if self.sword.crashed and not self.sword.get:
                        self.player.attack += 10
                        self.sword.get = True
                    if self.shield.crashed and not self.shield.get:
                        self.player.hp += 50
                        self.player.max_hp += 50
                        self.shield.get = True
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
                        if self.npc.crashed and pressed_key == K_y:
                            self.npc.get = True
                            self.player.skill = True
            if self.fade_scene.get_out():
                scene_exit = True
            if self.win_pos_x < 0:
                self.win_pos_x = 0
            if self.win_pos_y < 0:
                self.win_pos_y = 0
            if self.win_pos_x > 4680 - 800:
                self.win_pos_x = 4680 - 800
            if self.win_pos_y > 4360 - 600:
                self.win_pos_y = 4360 - 600
            if self.fade_scene.status != SceneStatus.Out:
                self.npc.collide(self.player)
                self.monster.collide(self.player)
                if not self.sword.get:
                    self.sword.collide(self.player)
                if not self.shield.get:
                    self.shield.collide(self.player)
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
