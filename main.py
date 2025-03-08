import pygame
import sys

from consts import BG_COLOR, FPS
from screen_text import ScreenText


pygame.init()

info = pygame.display.Info()
screen_size = info.current_w - info.current_w * 0.3, info.current_h - info.current_h * 0.3

screen = pygame.display.set_mode(
    screen_size, pygame.RESIZABLE)
pygame.display.set_caption("TypoCode")

screen_text = ScreenText(screen)

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
    screen_text.draw()

    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)
