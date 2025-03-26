import sys
import pygame
from pygame.key import ScancodeWrapper
import pygame_gui
from common.common import update_events
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

icon = pygame.image.load("./src/_content/icons/keyboard_32x32.png")
pygame.display.set_icon(icon)

start_screen_size = screen.size
min_screen_size = (1280, 800)

manager = pygame_gui.UIManager(
    start_screen_size,
    enable_live_theme_updates=True,
    theme_path="src/ui/theme.json"
)

game_state = GameState()

clock = pygame.time.Clock()


while True:
    start_window = StartWindow(game_state, manager)
    start_window.show(screen, start_screen_size, clock, min_screen_size)

    typing_window = TypingWindow(game_state)
    typing_window.show(screen, clock, min_screen_size)

    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)
