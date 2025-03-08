import pygame
import sys

from consts import BG_COLOR, FPS
from text_generator import TextGenerator
from ui.main_window import MainWindow


pygame.init()

info = pygame.display.Info()
screen_size = info.current_w - info.current_w * 0.3, info.current_h - info.current_h * 0.3

screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
pygame.display.set_caption("TypoCode")

text_generator = TextGenerator()
screen_text = MainWindow()

clock = pygame.time.Clock()

while True:

    screen.fill(BG_COLOR)

    keys = pygame.key.get_pressed()

    events = pygame.event.get()

    for event in events:
        if keys[pygame.K_ESCAPE] or event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen_text.update(events)
    screen_text.draw(screen)

    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)
