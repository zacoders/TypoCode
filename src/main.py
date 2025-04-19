import os
import sys
import pygame
from common.common import get_resource_path, is_linux, is_windows
from game_state import GameState
from ui.help_window import HelpWindow
from ui.theme_config import save_theme
from ui.typing_window import TypingWindow
from ui.start_window import StartWindow
import ctypes

if is_linux() and "SDL_AUDIODRIVER" not in os.environ:
    os.environ["SDL_AUDIODRIVER"] = "dummy"  # Set only if not defined

# Set process DPI awareness. Use 1 for "System DPI Awareness", or 2 for "Per-Monitor DPI Awareness"
if is_windows():
    ctypes.windll.shcore.SetProcessDpiAwareness(1)

print(f'{sys.executable=}')
print(f'{pygame.__version__=}')

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=100)

info = pygame.display.Info()

max_screen_size = (info.current_w, info.current_h)
min_screen_size = (1280, 800)

screen_size = info.current_w * 0.7, info.current_h * 0.7

screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
pygame.display.set_caption("TypoCode")

icon = pygame.image.load(get_resource_path("./src/keyboard_32x32.png"))
pygame.display.set_icon(icon)

start_screen_size = screen.size

save_theme()

game_state = GameState()

clock = pygame.time.Clock()

while True:
    help_window = HelpWindow()
    help_window.show(screen, clock, min_screen_size, max_screen_size)

    start_window = StartWindow(game_state)
    start_window.show(screen, start_screen_size, clock, min_screen_size, max_screen_size)

    typing_window = TypingWindow(game_state)
    typing_window.show(screen, clock, min_screen_size, max_screen_size)
