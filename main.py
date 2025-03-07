import pygame
import sys

from consts import BG_COLOR, FPS, START_SCREEN_HEIGHT, START_SCREEN_WIDTH
from screen_text import ScreenText


pygame.init()

screen: pygame.Surface = pygame.display.set_mode((START_SCREEN_WIDTH, START_SCREEN_HEIGHT), pygame.RESIZABLE)
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

    screen_text.update(events, keys)
    screen_text.draw()

    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)
