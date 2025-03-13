import pygame

from typing import Callable, Tuple


class Button:
    def __init__(self, size: Tuple[int, int], text: str, action: Callable[[], None]):
        self.image = pygame.image.load('images/menus/button.png').convert()
        self.image = pygame.transform.scale(self.image, size)
        self.image.set_colorkey((0, 0, 0))

        font = pygame.font.Font("fonts/UbuntuMono-Regular.ttf", round(25))  # Use `round` for exact size
        self.text = font.render(text, False, (255, 255, 255))

        self.clicked = False

        self.action = action

    def set_position(self, pos):
        self.rect = self.image.get_rect(center=pos)
        self.text_rect = self.text.get_rect(center=self.rect.center)

    def update(self, event: pygame.event.Event):
        if self.is_clicked(event):
            self.action()

    def is_clicked(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.collide(event.pos):
                self.clicked = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and self.clicked and self.collide(event.pos):
                self.clicked = False
                return True
        return False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def collide(self, mouse_pos: Tuple[int, int]) -> bool:
        return self.rect.collidepoint(mouse_pos)
