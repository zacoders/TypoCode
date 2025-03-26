import sys
from typing import List
from pygame.event import Event
from pygame import Surface
import pygame

from game_state import GameState


def update_events(events: List[Event], game_state: GameState, keys, screen: Surface):
    screen = screen
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif keys[pygame.K_ESCAPE]:
            if game_state.is_started:
                game_state.is_started = False
        elif event.type == pygame.VIDEORESIZE:
            new_width, new_height = event.w, event.h
            screen = pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)


def is_capslock_on():
    if sys.platform.startswith("win"):
        import ctypes
        return bool(ctypes.windll.user32.GetKeyState(0x14) & 1)

    elif sys.platform.startswith("linux"):
        try:
            from Xlib import display
            d = display.Display()
            return bool(d.get_keyboard_control().leds & 1)
        except ImportError:
            raise RuntimeError(
                "Для работы на Linux требуется пакет python-xlib. Установите его: pip install python-xlib")

    else:
        raise NotImplementedError("Поддерживаются только Windows и Linux")


def is_shift_pressed():
    if sys.platform.startswith("win"):
        import ctypes
        return bool(ctypes.windll.user32.GetKeyState(0x10) & 0x8000)

    elif sys.platform.startswith("linux"):
        try:
            from Xlib import display, X
            d = display.Display()
            state = d.query_keymap()
            shift_keycode = d.keysym_to_keycode(X.XK_Shift_L)  # Левая Shift
            shift_r_keycode = d.keysym_to_keycode(X.XK_Shift_R)  # Правая Shift
            return bool(state[shift_keycode // 8] & (1 << (shift_keycode % 8))) or \
                bool(state[shift_r_keycode // 8] & (1 << (shift_r_keycode % 8)))
        except ImportError:
            raise RuntimeError(
                "Для работы на Linux требуется пакет python-xlib. Установите его: pip install python-xlib")

    else:
        raise NotImplementedError("Поддерживаются только Windows и Linux")
