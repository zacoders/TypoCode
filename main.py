import pygame
import sys
from consts import BG_COLOR, FPS
from game_state import GameState
from ui.main_window import MainWindow
from ui.menus.main_menu import MainMenu


pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=100)

info = pygame.display.Info()
screen_size = info.current_w - info.current_w * 0.3, info.current_h - info.current_h * 0.3

screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
pygame.display.set_caption("TypoCode")

game_state = GameState()

main_window = MainWindow(game_state)

clock = pygame.time.Clock()

game_state.active_screen = MainMenu(main_window.get_text_generator(), game_state, screen)

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

    if game_state.active_screen is not None:
        game_state.active_screen.update(events)
        if hasattr(game_state.active_screen, "draw"):
            game_state.active_screen.draw()
        else:
            print("Ошибка: active_screen стал None перед вызовом draw()")
    else:
        main_window.update(events, screen.get_height(), screen.get_width())
        main_window.draw(screen)

    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)
