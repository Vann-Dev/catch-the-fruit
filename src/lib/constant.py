import random

car = "🚗"
road = "🟫"
door = "🚪"

# 2 menit 64*32
# 45 detik 32*16

# 1.30 menit dark 32*16
# 5 menit dark 64*32

modes = {
    "normal": {"height": 16, "width": 32, "fruit": 10, "fogg": False},
    "normal_dark": {"height": 16, "width": 32, "fruit": 10, "fogg": True},
    "tutorial": {"height": 5, "width": 10, "fruit": 2, "fogg": False},
    "big": {"height": 32, "width": 64, "fruit": 50, "fogg": False},
    "big_dark": {"height": 32, "width": 64, "fruit": 50, "fogg": True},
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
