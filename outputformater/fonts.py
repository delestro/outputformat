# List of characters suported
# Every new font must include these
suported_chars = "0123456789abcdefghijklmnopqrstuvwxyz_-!. "

# Small font
# █▀█ ▄█ ▀█ ▀▀█ █ █ █▀ █▄▄ ▀▀█ █▀█ █▀█
# █▄█  █ █▄ ▄██ ▀▀█ ▄█ █▄█   █ ███ ▀▀█
#
# ▄▀█ █▄▄ █▀▀ █▀▄
# █▀█ █▄█ █▄▄ █▄▀
#
# █▀▀ █▀▀ █▀▀ █ █
# ██▄ █▀  █▄█ █▀█
#
# █   █ █▄▀ █
# █ █▄█ █ █ █▄▄
#
# █▀▄▀█ █▄ █ █▀█ █▀█
# █ ▀ █ █ ▀█ █▄█ █▀▀
#
# █▀█ █▀█ █▀ ▀█▀
# ▀▀█ █▀▄ ▄█  █
#
# █ █ █ █ █ █ █
# █▄█ ▀▄▀ ▀▄▀▄▀
#
# ▀▄▀ █▄█ ▀█
# █ █  █  █▄

small = {
    "nrows": 2,
    "0": ["█▀█", "█▄█"],
    "1": ["▄█", " █"],
    "2": ["▀█", "█▄"],
    "3": ["▀▀█", "▄██"],
    "4": ["█ █", "▀▀█"],
    "5": ["█▀", "▄█"],
    "6": ["█▄▄", "█▄█"],
    "7": ["▀▀█", "  █"],
    "8": ["█▀█", "███"],
    "9": ["█▀█", "▀▀█"],
    "a": ["▄▀█", "█▀█"],
    "b": ["█▄▄", "█▄█"],
    "c": ["█▀▀", "█▄▄"],
    "d": ["█▀▄", "█▄▀"],
    "e": ["█▀▀", "██▄"],
    "f": ["█▀▀", "█▀ "],
    "g": ["█▀▀", "█▄█"],
    "h": ["█ █", "█▀█"],
    "i": ["█", "█"],
    "j": ["  █", "█▄█"],
    "k": ["█▄▀", "█ █"],
    "l": ["█  ", "█▄▄"],
    "m": ["█▀▄▀█", "█ ▀ █"],
    "n": ["█▄ █", "█ ▀█"],
    "o": ["█▀█", "█▄█"],
    "p": ["█▀█", "█▀▀"],
    "q": ["█▀█", "▀▀█"],
    "r": ["█▀█", "█▀▄"],
    "s": ["█▀", "▄█"],
    "t": ["▀█▀", " █ "],
    "u": ["█ █", "█▄█"],
    "v": ["█ █", "▀▄▀"],
    "w": ["█ █ █", "▀▄▀▄▀"],
    "x": ["▀▄▀", "█ █"],
    "y": ["█▄█", " █ "],
    "z": ["▀█", "█▄"],
    "_": ["   ", "▄▄▄"],
    "-": ["  ", "▀▀"],
    "!": ["█", "▄"],
    ".": [" ", "▄"],
    " ": [" ", " "],
}