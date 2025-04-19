

from typing import Tuple
import pygame
from pygame import Surface

from common.common import get_resource_path
from ui.fingers_enum import FingersEnum


class HandsAnimator:

    WIDTH_SCALE = 0.46
    HEIGHT_SCALE = 0.54

    def __init__(self):
        self.__original_hands_image = pygame.image.load(
            get_resource_path("src/_content/images/arms/arms.png")
        )
        self.__hands_image = self.__original_hands_image

        self.__fingers = {
            FingersEnum.LEFT_LITTLE: self.__load_finger("left_little_finger"),
            FingersEnum.LEFT_RING: self.__load_finger("left_ring_finger"),
            FingersEnum.LEFT_MIDDLE: self.__load_finger("left_middle_finger"),
            FingersEnum.LEFT_INDEX: self.__load_finger("left_index_finger"),
            FingersEnum.BOTH_THUMBS: self.__load_finger("thumbs"),
            FingersEnum.RIGHT_INDEX: self.__load_finger("right_index_finger"),
            FingersEnum.RIGHT_MIDDLE: self.__load_finger("right_middle_finger"),
            FingersEnum.RIGHT_RING: self.__load_finger("right_ring_finger"),
            FingersEnum.RIGHT_LITTLE: self.__load_finger("right_little_finger"),
            FingersEnum.BOTH_INDEXES: self.__load_finger("start_buttons_fingers")
        }

        self.__draw_sequence = list(self.__fingers.keys())

        self.__finger_enum = FingersEnum.LEFT_LITTLE
        self.__draw_finger = 0
        self.__blinks_num = 0
        self.__is_visible = True
        self.__last_blink_time = pygame.time.get_ticks()
        self.__blink_delay = 500

    def __load_finger(self, file_name: str) -> Surface:
        root = "src/_content/images/arms/"
        return pygame.image.load(get_resource_path(root + file_name + '.png'))

    def __get_scale(self, image_size: Tuple[int, int], screen_size: Tuple[int, int]):
        scale_w = image_size[0] / screen_size[0] / self.WIDTH_SCALE
        scale_h = image_size[1] / screen_size[1] / self.HEIGHT_SCALE
        return scale_w, scale_h

    def update(self):

        now = pygame.time.get_ticks()
        if now - self.__last_blink_time >= self.__blink_delay:
            self.__last_blink_time = now
            self.__is_visible = not self.__is_visible  # мигаем

            if not self.__is_visible:
                self.__blinks_num += 1

            if self.__blinks_num >= 3:
                self.__blinks_num = 0
                self.__draw_finger += 1
                self.__is_visible = True

            if self.__draw_finger > len(self.__draw_sequence) - 1:
                self.__draw_finger = 0

    def draw(self, screen: Surface):
        scale_w, scale_h = self.__get_scale(
            (self.__original_hands_image.get_size()),
            (screen.get_size())
        )

        scale = max(scale_w, scale_h)

        self.__hands_image = pygame.transform.scale(
            self.__original_hands_image,
            (
                int(self.__original_hands_image.get_width() / scale),
                int(self.__original_hands_image.get_height() / scale)
            )
        )

        hands_x = screen.get_width() // 2 - self.__hands_image.get_width() // 2
        hands_y = screen.get_height() - self.__hands_image.get_height() + 75

        screen.blit(self.__hands_image, (hands_x, hands_y))

        if self.__is_visible:
            finger: FingersEnum = self.__draw_sequence[self.__draw_finger]
            self.__finger_enum = finger
            image = self.__fingers[finger]
            finger_image = pygame.transform.scale(
                image,
                (
                    int(image.get_width() / scale),
                    int(image.get_height() / scale)
                )
            )
            screen.blit(finger_image, (hands_x, hands_y))

    def get_finger_enum(self):
        return self.__finger_enum
