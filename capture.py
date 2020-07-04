"""
# >>> Author: WindCry1
# >>> Mail: lanceyu120@gmail.com
# >>> Website: https://windcry1.com
# >>> Date: 2020/7/3 13:55
"""


import pygame
pygame.init()
image_path = 'resources/img/npc/origin.png'
save_path = 'resources/img/npc/'
image_width = 128
image_height = 192
image = pygame.image.load(image_path)
surface = pygame.display.set_mode((image_width, image_height))
surface.fill((255, 255, 255))
surface.blit(image, (0, 0))
for i in range(0, 4):
    for j in range(0, 4):
        width = image_width//4*i
        height = image_height//4*j
        capture = surface.subsurface(pygame.Rect(width, height, image_width//4, image_height//4))
        pygame.image.save(capture, save_path + '%02d' % j + '%03d' % i + '.png')
