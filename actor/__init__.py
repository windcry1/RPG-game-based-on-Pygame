"""
# >>> Author: WindCry1
# >>> Mail: lanceyu120@gmail.com
# >>> Website: https://windcry1.com
# >>> Date: 2020/7/3 10:51
"""

import pygame
import os


class DirAction:
    def __init__(self, path_name1: str, path_name2: str,
                 prefix: str, dir_count: int, frame_count: int, is_loop: bool):
        """
        角色动画效果
        :param path_name1 : 上一层文件夹名
        :param path_name2 : 本层文件夹名
        :param prefix : 文件名前缀
        :param dir_count : 方向数量
        :param frame_count : 该方向上的帧数量
        :param is_loop : 是否循环
        """
        self.name = path_name1
        self.image_index = 0
        self.action_images = []
        self.frame_count = frame_count
        self.dir = 0
        self.is_loop = is_loop
        for j in range(dir_count):
            dir_image = []
            for i in range(frame_count):
                img_path = os.path.join('resources', 'img', path_name1, path_name2,
                                        prefix + str.format("%02d" % j) + str.format("%03d" % i) + '.png')
                img = pygame.image.load(img_path).convert()
                img.set_colorkey((255, 255, 255))
                dir_image.append(img)
            self.action_images.append(dir_image)

    def get_curr_frame(self, dir):
        current_img = self.action_images[dir][self.image_index]
        if self.image_index + 1 >= self.frame_count:
            if self.is_loop:
                self.image_index = 0
        else:
            self.image_index += 1
        return current_img

    def is_end(self):
        if self.is_loop:
            return False
        else:
            if self.image_index >= self.frame_count - 1:
                return True
            else:
                return False

    def reset(self):
        self.image_index = 0
