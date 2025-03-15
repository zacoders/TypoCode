import sys
import pygame
import pygame_gui
from common import update_events
from consts import BG_COLOR, FPS
from game_state import GameState
from ui.main_window import MainWindow
from ui.buttons_window import ButtonsWindow

print(f'{sys.executable=}')
print(f'{pygame.__version__=}')

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=100)

info = pygame.display.Info()
screen_size = info.current_w - info.current_w * 0.3, info.current_h - info.current_h * 0.3

screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
pygame.display.set_caption("TypoCode")

manager = pygame_gui.UIManager((screen.get_width(), screen.get_height()), theme_path="ui_theme.json")


game_state = GameState()

clock = pygame.time.Clock()


window = ButtonsWindow(game_state, manager)

while not game_state.is_started:
    screen.fill(BG_COLOR)

    events = pygame.event.get()
    keys = pygame.key.get_pressed()

    update_events(events, keys, screen)

    for event in events:
        manager.process_events(event)

    time_delta = clock.tick(FPS) / 1000.0

    window.update(events)

    manager.update(time_delta)
    manager.draw_ui(screen)

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
