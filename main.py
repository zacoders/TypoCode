import sys
import pygame
import pygame_gui
from common import update_events
from consts import BG_COLOR, FPS
from game_state import GameState
from ui.main_window import MainWindow
from ui.menus.main_menu import MainMenu

print(f'{sys.executable=}')
print(f'{pygame.__version__=}')

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=100)

info = pygame.display.Info()
screen_size = info.current_w - info.current_w * 0.3, info.current_h - info.current_h * 0.3

screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
pygame.display.set_caption("TypoCode")

manager = pygame_gui.UIManager((400, 300))

game_state = GameState()

clock = pygame.time.Clock()


game_state.active_screen = MainMenu(game_state, manager, screen)

while game_state.active_screen is not None:
    screen.fill(BG_COLOR)

    events = pygame.event.get()
    keys = pygame.key.get_pressed()

    update_events(events, keys, screen)

    for event in events:
        manager.process_events(event)

    game_state.active_screen.draw()
    game_state.active_screen.update(events)

    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)


main_window = MainWindow(game_state)

while True:

    screen.fill(BG_COLOR)

    keys = pygame.key.get_pressed()

    events = pygame.event.get()

    update_events(events, keys, screen)

    main_window.update(events, screen.get_height(), screen.get_width())
    main_window.draw(screen)

    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)
