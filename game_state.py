
from generators.c_sharp import CSharpGenerator
from generators.python import PythonGenerator
from generators.russian import RussianGenerator
from ui.menus.basic.screen import ScreenABC


class GameState:

    active_screen: ScreenABC | None = None
    generator: PythonGenerator | CSharpGenerator | RussianGenerator = RussianGenerator()
