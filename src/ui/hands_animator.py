

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
            get_resource_path("src/_content/images/arms/arms.png"))
        self.__hands_image = self.__original_hands_image

        self.__finger_images = [
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

        self.__fingers = {}

        for image in self.__finger_images:
            finger = pygame.image.load(get_resource_path(image))
            finger_name = f"{image[image.rfind('/') + 1:-4]}"

            self.__fingers[finger_name] = finger

        self.__fingers_enums = [
            (self.__fingers["left_little_finger"], FingersEnum.LEFT_LITTLE),
            (self.__fingers["left_ring_finger"], FingersEnum.LEFT_RING),
            (self.__fingers["left_middle_finger"], FingersEnum.LEFT_MIDDLE),
            (self.__fingers["left_index_finger"], FingersEnum.LEFT_INDEX),
            (self.__fingers["left_thumb"], FingersEnum.LEFT_THUMB),
            (self.__fingers["right_thumb"], FingersEnum.RIGHT_THUMB),
            (self.__fingers["right_index_finger"], FingersEnum.RIGHT_INDEX),
            (self.__fingers["right_middle_finger"], FingersEnum.RIGHT_MIDDLE),
            (self.__fingers["right_ring_finger"], FingersEnum.RIGHT_RING),
            (self.__fingers["right_little_finger"], FingersEnum.RIGHT_LITTLE),
            (self.__fingers["start_buttons_fingers"], FingersEnum.START_BUTTONS)
        ]

        self.__finger_enum = FingersEnum.LEFT_LITTLE
        self.__drew_fingers = 0
        self.__blinks_num = 0
        self.__is_visible = True
        self.__last_blink_time = pygame.time.get_ticks()
        self.__blink_delay = 500

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
                self.__drew_fingers += 1
                self.__is_visible = True

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

        if self.__drew_fingers < len(self.__fingers_enums) and self.__is_visible:
            finger_image, self.__finger_enum = self.__fingers_enums[self.__drew_fingers]
            finger_image = pygame.transform.scale(
                finger_image,
                (
                    int(finger_image.get_width() / scale),
                    int(finger_image.get_height() / scale)
                )
            )
            screen.blit(finger_image, (hands_x, hands_y))

    def get_finger_enum(self):
        return self.__finger_enum
    
    def get_hands_image(self):
        return self.__hands_image
