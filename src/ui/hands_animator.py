

from typing import Tuple
import pygame
from pygame import Event, Surface
from consts import FINGER_BLINK_TIME_MS
from ui.fingers_enum import FingersEnum
from ui.images_loader import ImagesLoader


class HandsAnimator:

    WIDTH_SCALE = 0.46
    HEIGHT_SCALE = 0.54

    def __init__(self, relative_y_pos: float, images_loader: ImagesLoader):

        self.__relative_y_pos = relative_y_pos

        self.__images_loader = images_loader

        self.__original_hands_image = self.__images_loader.get_image("src/_content/images/hands/hands.png")
        self.__hands_image = self.__original_hands_image

        self.__fingers = {
            FingersEnum.BOTH_INDEXES: self.__load_finger("start_buttons_fingers"),
            FingersEnum.LEFT_LITTLE: self.__load_finger("left_little_finger"),
            FingersEnum.LEFT_RING: self.__load_finger("left_ring_finger"),
            FingersEnum.LEFT_MIDDLE: self.__load_finger("left_middle_finger"),
            FingersEnum.LEFT_INDEX: self.__load_finger("left_index_finger"),
            FingersEnum.LEFT_THUMB: self.__load_finger("left_thumb"),
            FingersEnum.RIGHT_THUMB: self.__load_finger("right_thumb"),
            FingersEnum.RIGHT_INDEX: self.__load_finger("right_index_finger"),
            FingersEnum.RIGHT_MIDDLE: self.__load_finger("right_middle_finger"),
            FingersEnum.RIGHT_RING: self.__load_finger("right_ring_finger"),
            FingersEnum.RIGHT_LITTLE: self.__load_finger("right_little_finger")
        }

        self.__draw_sequence = list(self.__fingers.keys())
        self.__draw_sequence_len = len(self.__draw_sequence)

        self.__finger_enum = FingersEnum.BOTH_INDEXES
        self.__draw_finger = 0
        self.__blinks_num = 0
        self.__is_visible = False
        self.__next_blink_time: int = pygame.time.get_ticks()
        self.__blink_delay = FINGER_BLINK_TIME_MS
        self.__repeat = False

    def __load_finger(self, file_name: str) -> Surface:
        root = "src/_content/images/hands/"
        return self.__images_loader.get_image(root + file_name + '.png')

    def __get_scale(self, image_size: Tuple[int, int], screen_size: Tuple[int, int]):
        scale_w = image_size[0] / screen_size[0] / self.WIDTH_SCALE
        scale_h = image_size[1] / screen_size[1] / self.HEIGHT_SCALE
        return max(scale_w, scale_h)

    def __reset_blink(self):
        self.__next_blink_time = 0
        self.__blinks_num = 0
        self.__is_visible = False

    def update(self, events: list[Event]):

        now = pygame.time.get_ticks()

        for event in events:
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_LEFT:
                self.__draw_finger -= 1
                self.__reset_blink()
            if event.key == pygame.K_RIGHT:
                self.__draw_finger += 1
                self.__reset_blink()

        if now < self.__next_blink_time:
            return

        self.__next_blink_time = now + self.__blink_delay
        self.__is_visible = not self.__is_visible  # мигаем

        if not self.__is_visible:
            self.__blinks_num += 1

        if self.__blinks_num >= 3:
            self.__blinks_num = 0
            self.__draw_finger += 1
            if self.__draw_finger > self.__draw_sequence_len - 1:
                self.__repeat = True
            self.__is_visible = True

        if self.__draw_finger < 0:
            self.__draw_finger = self.__draw_sequence_len - 1

        if self.__draw_finger > self.__draw_sequence_len - 1:
            self.__draw_finger = 0

    def draw(self, screen: Surface):
        scale = self.__get_scale(
            self.__original_hands_image.get_size(),
            screen.get_size()
        )

        self.__hands_image = pygame.transform.scale(
            self.__original_hands_image,
            (
                int(self.__original_hands_image.get_width() / scale),
                int(self.__original_hands_image.get_height() / scale)
            )
        )

        hands_x = screen.get_width() // 2 - self.__hands_image.get_width() // 2
        hands_y = screen.height * self.__relative_y_pos

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

    def get_finger(self):
        return self.__finger_enum

    def is_visible(self):
        return self.__is_visible

    def is_repeat(self):
        return self.__repeat

    def restart(self):
        self.__repeat = False
        self.__blinks_num = 0
        self.__draw_finger = 0
        self.__is_visible = False
        self.__next_blink_time = pygame.time.get_ticks() + self.__blink_delay
