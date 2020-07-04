import pygame
import tiled_render as tiled
from pytmx import *
from pygame.constants import QUIT
from pytmx.util_pygame import load_pygame


class TileScene:
    def __init__(self, path):
        self.tiled_path = path
        self.tiled = tiled.TiledRenderer(self.tiled_path)
        self.surface = pygame.Surface(self.tiled.pixel_size)
        self.tiled.render_map(self.surface)

    def render_without_object(self):
        self.surface = pygame.Surface(self.tiled.pixel_size)
        if self.tiled.tmx_data.background_color:
            surface.fill(pygame.Color(self.tiled.tmx_data.background_color))
        for layer in self.tiled.tmx_data.visible_layers:
            if isinstance(layer, TiledTileLayer):
                self.tiled.render_tile_layer(self.surface, layer)
            elif isinstance(layer, TiledImageLayer):
                self.tiled.render_image_layer(self.surface, layer)

    def get_size(self):
        return self.surface.get_width(), self.surface.get_height()

    def show_scene(self, screen):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
            screen.blit(self.surface, (0, 0))
            pygame.display.update()
