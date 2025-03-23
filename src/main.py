import sys
import pygame
from pygame.key import ScancodeWrapper
import pygame_gui
from common.common import get_resource_path, update_events
from consts import BG_COLOR, FPS
from game_state import GameState
from ui.typing_window import TypingWindow
from ui.start_window import StartWindow
import ctypes

# Set process DPI awareness. Use 1 for "System DPI Awareness", or 2 for "Per-Monitor DPI Awareness"
ctypes.windll.shcore.SetProcessDpiAwareness(1)

print(f'{sys.executable=}')
print(f'{pygame.__version__=}')

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=100)

info = pygame.display.Info()
screen_size = info.current_w * 0.7, info.current_h * 0.7

screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
pygame.display.set_caption("TypoCode")

start_screen_size = screen.size

manager = pygame_gui.UIManager(
    start_screen_size,
    enable_live_theme_updates=True,
    theme_path=get_resource_path("src/_content/theme.json")
)

game_state = GameState()

clock = pygame.time.Clock()


start_window = StartWindow(game_state, manager)

while not game_state.is_started:
    screen.fill(BG_COLOR)

    events = pygame.event.get()
    keys = pygame.key.get_pressed()

    update_events(events, keys, screen)

    time_delta = clock.tick(FPS) / 1000.0

    start_window.update(events, screen.get_width(), screen.get_height())

    if start_screen_size != screen.size:
        manager.set_window_resolution(screen.size)

    for event in events:
        manager.process_events(event)

    manager.draw_ui(screen)
    manager.update(time_delta)

    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)


typing_window = TypingWindow(game_state)

while True:

    screen.fill(BG_COLOR)

    keys: ScancodeWrapper = pygame.key.get_pressed()

    events = pygame.event.get()

    update_events(events, keys, screen)

    typing_window.update(events, keys, screen.get_height(), screen.get_width())
    typing_window.draw(screen)

    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)
