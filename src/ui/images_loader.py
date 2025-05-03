import os
from typing import Dict
import pygame

from common.common import get_resource_path


class ImagesLoader:
    def __init__(self):
        folders = self.__get_folders()
        self.__images: dict[str, pygame.Surface] = self.__load_images(folders)

    def __get_folders(self) -> list[str]:
        base_path = "src/_content/images"
        folders = []
        for folder in os.listdir(base_path):
            full_path = os.path.join(base_path, folder)
            if os.path.isdir(full_path):
                folders.append(full_path)
        return folders

    def __load_images(self, folders: list[str]) -> dict[str, pygame.Surface]:
        images = {}
        for folder in folders:
            for filename in os.listdir(folder):
                path = os.path.join(folder, filename).replace("\\", "/")
                image = pygame.image.load(get_resource_path(path)).convert_alpha()
                images[path] = image
        return images

    def get_image(self, path: str) -> pygame.Surface:
        return self.__images[path]
