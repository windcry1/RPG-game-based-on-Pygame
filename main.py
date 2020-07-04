"""
# >>> Author: WindCry1
# >>> Mail: lanceyu120@gmail.com
# >>> Website: https://windcry1.com
# >>> Date: 2020/7/3 10:22
"""
import pygame
from scene.scene0 import Scene0
from scene.scene1 import Scene1
from scene.scene2 import Scene2
from scene.the_end_scene import TheEndScene
from scene import SceneResult

pygame.init()
screen = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('魔界勇士之拯救天庭篇')
scene0 = Scene0(screen)
scene0.run()
scene1 = Scene1(screen)
scene1.run()
is_win = False
if scene1.scene_result == SceneResult.Win:
    scene2 = Scene2(scene1.player, screen)
    scene2.run()
    if scene2.scene_result == SceneResult.Win:
        is_win = True
the_end_scene = TheEndScene(is_win, screen)
the_end_scene.run()
pygame.quit()
