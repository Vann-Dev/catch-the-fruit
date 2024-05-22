import random

car = "🚗"
road = "🟫"
door = "🚪"

modes = {
    "normal": {"height": 16, "width": 32, "fruit": 10, "fogg": False},
    "normal_dark": {"height": 16, "width": 32, "fruit": 10, "fogg": True},
    "tutorial": {"height": 5, "width": 10, "fruit": 2, "fogg": False},
    "big": {"height": 32, "width": 64, "fruit": 50, "fogg": False},
    "big_dark": {"height": 32, "width": 64, "fruit": 50, "fogg": True},
}

colors = [
    "\033[31m",
    "\033[32m",
    "\033[33m",
    "\033[33m",
    "\033[34m",
    "\033[35m",
    "\033[36m",
]

screens = {
    "home": "home_screen",
    "tutorial": "tutorial_screen",
    "credit": "credit_screen",
    "select": "select_mode",
    "game": "game_screen",
    "pause": "pause_screen",
}


def border():
    borders = [
        "🧱",
    ]

    return random.choice(borders)


fruits = [
    "🍎",
    "🍏",
    "🍐",
    "🍊",
    "🍋",
    "🍌",
    "🍉",
    "🍇",
    "🍓",
    "🍈",
    "🍒",
    "🍑",
    "🥭",
    "🍍",
    "🥥",
    "🥝",
    "🍅",
]


def fruit():
    return random.choice(fruits)


def tree():
    trees = [
        "🌳",
        "🌴",
        "🌵",
    ]

    return random.choice(trees)


def building():
    buildings = [
        "🏢",
        "🏦",
        "🏫",
        "🏨",
        "🏭",
        "🏪",
        "🏬",
        "🏯",
        "🏰",
        "🏩",
    ]

    return random.choice(buildings)
