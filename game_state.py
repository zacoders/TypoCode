
from generators.base import BaseGenerator
from generators.russian import RussianGenerator
from ui.menus.basic.screen import ScreenABC


class GameState:

    active_screen: ScreenABC | None = None
    generator: BaseGenerator = RussianGenerator()
