
import json
from common.common import get_resource_path


theme_config = {
    "button": {
        "font": {
            "name": "UbuntuMono-Regular",
            "size": 66,
            "regular_path": get_resource_path("src/_content/fonts/UbuntuMono-Regular.ttf")
        },
        "colours": {
            "normal_bg": "#003514",
            "hovered_bg": "#004F1E",
            "disabled_bg": "#66BB6A",
            "selected_bg": "#388E3C",
            "active_bg": "#388E3C",
            "normal_text": "#FFFFFF",
            "hovered_text": "#FFFFFF",
            "selected_text": "#FFFFFF",
            "disabled_text": "#A5D6A7",
            "active_text": "#FFFFFF",
            "normal_border": "#388E3C",
            "hovered_border": "#2C6B2F",
            "disabled_border": "#81C784",
            "selected_border": "#388E3C",
            "active_border": "#2C6B2F",
            "normal_text_shadow": "#10101070",
            "hovered_text_shadow": "#10101070",
            "disabled_text_shadow": "#10101070",
            "selected_text_shadow": "#10101070",
            "active_text_shadow": "#10101070"
        },
        "misc": {
            "shape": "rounded_rectangle",
            "shape_corner_radius": "10",
            "border_width": "2"
        }
    },
    "selection_list": {
        "colours": {
            "dark_bg": "#141414"
        },
        "misc": {
            "list_item_height": "115"
        }
    }
}

theme_path = get_resource_path("src/_content/theme.uitheme")


def get_theme_path(): return theme_path


def save_theme():
    with open(theme_path, "w", encoding="utf-8") as file:
        json.dump(theme_config, file, indent=4)
