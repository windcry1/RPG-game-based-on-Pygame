"""
# >>> Author: WindCry1
# >>> Mail: lanceyu120@gmail.com
# >>> Website: https://windcry1.com
# >>> Date: 2020/7/4 05:24
"""
import os
import pygame
from dialog import blit_text


class Dialog:
    def __init__(self, width, height, text, npc=False):
        header_h = 0
        header_w = 0
        if npc:
            img_path = os.path.join('resources', 'img', 'npc', '00000.png')
            temp_header = pygame.image.load(img_path)
            header_w = temp_header.get_width()//2
            header_h = temp_header.get_height()//2
            header = pygame.transform.scale(temp_header, (header_w, header_h))
        dialog_path = os.path.join('resources', 'img', 'dialog', 'dialog.png')
        temp_dialog = pygame.image.load(dialog_path)
        dialog_w = width
        dialog_h = height
        dialog = pygame.transform.scale(temp_dialog, (dialog_w, dialog_h))
        font_path = os.path.join('resources', 'font', 'msyh.ttf')
        font = pygame.font.Font(font_path, 18)
        blit_text(dialog, text, (20, 25), font, (0, 0, 1))
        h = max(header_h, dialog_h)
        w = header_w + dialog_w
        self.surface = pygame.Surface((w, h))
        self.surface.set_colorkey((0, 0, 0))
        if npc:
            self.surface.blit(header, (0, 0))
        self.surface.blit(dialog, (header_w, 0))
