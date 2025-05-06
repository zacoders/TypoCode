import pygame
from common.common import get_resource_path


class ImagesLoader:
    def __init__(self):
        self.__images: dict[str, pygame.Surface] = {}

    def get_image(self, path: str) -> pygame.Surface:
        if path in self.__images:
            return self.__images[path]
        image = pygame.image.load(get_resource_path(path)).convert_alpha()
        self.__images[path] = image
        return image
