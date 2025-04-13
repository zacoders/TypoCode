

from typing import List
import pygame
from pygame import Surface

from common.common import get_resource_path
from ui.fingers_enum import FingersEnum


class FingerAnimator:
    def __init__(self):
        images = [
            "src/_content/images/arms/left_thumb.png",
            "src/_content/images/arms/right_thumb.png",
            "src/_content/images/arms/left_index_finger.png",
            "src/_content/images/arms/right_index_finger.png",
            "src/_content/images/arms/left_middle_finger.png",
            "src/_content/images/arms/right_middle_finger.png",
            "src/_content/images/arms/left_ring_finger.png",
            "src/_content/images/arms/right_ring_finger.png",
            "src/_content/images/arms/left_little_finger.png",
            "src/_content/images/arms/right_little_finger.png",
            "src/_content/images/arms/start_buttons_fingers.png"
        ]

        fingers = {}

        for image in images:
            finger = pygame.image.load(get_resource_path(image))
            finger_name = f"{image[image.rfind('/') + 1:-4]}"

            finger_image = pygame.transform.scale(
                finger,
                (finger.width // 1.1, finger.height // 1.1)
            )

            fingers[finger_name] = finger_image

        self.__fingers_enums = [
            (fingers["left_little_finger"], FingersEnum.LEFT_LITTLE),
            (fingers["left_ring_finger"], FingersEnum.LEFT_RING),
            (fingers["left_middle_finger"], FingersEnum.LEFT_MIDDLE),
            (fingers["left_index_finger"], FingersEnum.LEFT_INDEX),
            (fingers["left_thumb"], FingersEnum.LEFT_THUMB),
            (fingers["right_thumb"], FingersEnum.RIGHT_THUMB),
            (fingers["right_index_finger"], FingersEnum.RIGHT_INDEX),
            (fingers["right_middle_finger"], FingersEnum.RIGHT_MIDDLE),
            (fingers["right_ring_finger"], FingersEnum.RIGHT_RING),
            (fingers["right_little_finger"], FingersEnum.RIGHT_LITTLE),
            (fingers["start_buttons_fingers"], FingersEnum.START_BUTTONS)
        ]

        self.__finger_enum = FingersEnum.LEFT_LITTLE
        self.__drew_fingers = 0
        self.__blinks_num = 0
        self.__is_visible = True
        self.__last_blink_time = pygame.time.get_ticks()
        self.__blink_delay = 500  # 0.5 секунды

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.__last_blink_time >= self.__blink_delay:
            self.__last_blink_time = now
            self.__is_visible = not self.__is_visible  # мигаем

            if not self.__is_visible:
                self.__blinks_num += 1

            if self.__blinks_num >= 3:
                self.__blinks_num = 0
                self.__drew_fingers += 1
                self.__is_visible = True

    def draw(self, screen: Surface, arms_image_size: tuple[int, int]) -> FingersEnum:
        if self.__drew_fingers < len(self.__fingers_enums) and self.__is_visible:
            finger_image, self.__finger_enum = self.__fingers_enums[self.__drew_fingers]
            screen.blit(
                finger_image,
                (
                    screen.get_width() // 2 - arms_image_size[0] // 2,
                    screen.get_height() - arms_image_size[1]
                )
            )
        return self.__finger_enum
    
    def get_finger_enum(self):
        return self.__finger_enum
