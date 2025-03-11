
from pygame.font import Font


class FontCalc:

    def __init__(self, font_file_path: str):
        self.__font_size = 100
        self.__prev_width = -1
        self.__font_file_path = font_file_path

    def current_font_size(self):
        return self.__font_size

    def update(self, text_len: int, screen_width: int):
        if screen_width != self.__prev_width:
            self.__font_size = self.__find_font_size(text_len, screen_width)
            self.__prev_width = screen_width

    def __find_font_size(self, text_len: int, screen_width: int) -> int:
        font_size = 100
        font = Font(self.__font_file_path, font_size)

        while True:
            render_text = font.render('0' * text_len, True, (0, 0, 0))
            text_width = render_text.get_rect().width

            if text_width < screen_width:
                break

            if text_width >= screen_width:
                font_size -= 1

            font = Font(self.__font_file_path, font_size)

        return font_size
