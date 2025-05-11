import pygame
from pygame.font import Font
from pygame import Surface, Clock
from pygame.key import ScancodeWrapper
from consts import BG_COLOR, FPS
from generators.keyboard_lang import KeyboardLanguage
from ui.hands_animator import HandsAnimator
from ui.images_loader import ImagesLoader
from ui.keyboard import Keyboard
from ui.window_abc import WindowABC
from pygame.typing import Point
from ui.font_calc import FontCalc
from common.common import get_resource_path


class HelpWindow(WindowABC):

    def __init__(self, images_loader: ImagesLoader):
        super().__init__()

        self.__keyboard = Keyboard(KeyboardLanguage.ENGLISH, relative_y_pos=0.025)
        self.__hands_animator = HandsAnimator(relative_y_pos=0.48, images_loader=images_loader)

        self.__font_file_path = get_resource_path("src/_content/fonts/UbuntuMono-Regular.ttf")
        self.__font_calc = FontCalc(self.__font_file_path)
        self.__font = Font(self.__font_file_path, 150)

        self.__text = 'F1 - Help;    F3 - Zen Mode;    F11 - Fulls Screen;    ESC - Exit'
        self.__text_color = (255, 255, 255)
        self.__text_line_color = (60, 60, 60)

    def update(self, keys: ScancodeWrapper, screen_width: int):
        self.__font_calc.update(len(self.__text), int(screen_width * 0.6))
        self.__hands_animator.update()
        self.__keyboard.update(keys)
        fingers_enum = self.__hands_animator.get_finger()
        is_visible = self.__hands_animator.is_visible()
        self.__keyboard.highlight_fingers_key(fingers_enum, is_visible)

    def draw(self, screen: Surface, font_size: int):
        self.__hands_animator.draw(screen)
        self.__keyboard.draw(screen)

        self.__font = Font(self.__font_file_path, font_size)

        line_rect = pygame.Rect(
            0,
            screen.get_height() - font_size,
            screen.get_width(),
            font_size
        )

        pygame.draw.rect(screen, self.__text_line_color, line_rect)

        text = self.__font.render(self.__text, True, self.__text_color)
        x, y = (screen.get_width() - text.get_width()) // 2, line_rect.y
        text_pos = (x, y)
        screen.blit(text, text_pos)

    def show(
        self,
        screen: Surface,
        clock: Clock,
        min_screen_size: Point,
        max_screen_size: Point,
        keyboard_lang: KeyboardLanguage
    ):
        self.__keyboard.set_language(keyboard_lang)
        self.__hands_animator.restart()
        while True:
            screen.fill(BG_COLOR)

            keys = pygame.key.get_pressed()
            events = pygame.event.get()

            self.update_events(events, screen, min_screen_size, max_screen_size)

            for event in events:
                if event.type == pygame.KEYDOWN and event.key != pygame.K_F11:
                    return
                if event.type == pygame.MOUSEBUTTONDOWN and event.button:
                    return

            if self.__hands_animator.is_repeat():
                return

            self.update(keys, screen.get_width())
            self.draw(screen, self.__font_calc.current_font_size())

            pygame.display.update()
            pygame.display.flip()
            clock.tick(FPS)
