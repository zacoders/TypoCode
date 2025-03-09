import pygame
import sys
from consts import BG_COLOR, FPS
from generators.python import PythonGenerator
from ui.main_window import MainWindow


pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=100)
# pygame.mixer.init()

info = pygame.display.Info()
screen_size = info.current_w - info.current_w * 0.3, info.current_h - info.current_h * 0.3

screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
pygame.display.set_caption("TypoCode")

text_generator = PythonGenerator()
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
        elif event.type == pygame.VIDEORESIZE:
            new_width, new_height = event.w, event.h
            screen = pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)

    screen_text.update(events, screen.get_width())
    screen_text.draw(screen)

    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)
