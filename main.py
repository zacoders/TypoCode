import pygame
import sys

from consts import BG_COLOR, FPS, START_SCREEN_HEIGHT, START_SCREEN_WIDTH


pygame.init()

screen: pygame.Surface = pygame.display.set_mode((START_SCREEN_WIDTH, START_SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("TypoCode")

clock = pygame.time.Clock()

while True:

    screen.fill(BG_COLOR)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if keys[pygame.K_ESCAPE] or event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    line_rect = pygame.Rect(0, screen.get_height()//2-25, screen.get_width(), 50)

    pygame.draw.rect(screen, (0, 0, 0), line_rect)

    pygame.display.update()

    pygame.display.flip()
    clock.tick(FPS)
