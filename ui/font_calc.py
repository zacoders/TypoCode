
from pygame.font import Font


class FontCalc:

    def __init__(self):
        self.__font_size = 100
        self.__prev_width = -1

    def current_font_size(self):
        return self.__font_size

    def update(self, text_len: int, screen_width: int):
        if screen_width != self.__prev_width:
            self.__font_size = self.__find_font_size(text_len, screen_width)
            self.__prev_width = screen_width

    def __find_font_size(self, text_len: int, screen_width: int) -> int:
        font_size = 100
        font = Font("fonts/Inconsolata-Regular.ttf", font_size)

        while True:
            render_text = font.render('0' * text_len, True, (0, 0, 0))
            text_width = render_text.get_rect().width

            if text_width < screen_width:
                break

            if text_width >= screen_width:
                font_size -= 1

            font = Font("fonts/Inconsolata-Regular.ttf", font_size)

        return font_size
