from outputformat.title import linetitle
from outputformat.title import boxtitle
from outputformat import emoji
import colorsys
from random import random


def prepare_data(input_data, precision):
    """
    Prepare the input data so that display is cleaner
    """

    data = input_data.copy()

    # Check if we have negative and positive values
    # If we don't have negative values, there's no point in adding "+"
    # To align the list
    negative_values = False
    for value in data:
        if isinstance(value, (int, float)) and value < 0:
            negative_values = True

    for idx, value in enumerate(data):

        # In case float, adjust precision
        if isinstance(value, float):
            data[idx] = f"{value:.{precision}f}"
            if negative_values and value > 0:
                data[idx] = "+" + data[idx]

        # In case int, just add "+" if needed
        if isinstance(value, int):
            data[idx] = f"{value}"
            if negative_values and value > 0:
                data[idx] = "+" + data[idx]

        # In case list, be recursive
        if isinstance(value, list):
            data[idx] = prepare_data(value, precision=precision)

    return data


def get_markers_and_title(style, title=False):

    if style in ["bullet", "bullets", "dot", "dots", ".", "*"]:
        marker_first = "•"
        marker_middle = "•"
        marker_last = "•"

    elif style in ["line", "-", "hang"]:
        marker_first = "╭"
        marker_middle = "├"
        marker_last = "╰"

        # Here we need a fancy title to go with the line
        if title:
            marker_first = marker_middle
            title = linetitle(title, style="hang", return_str=True)

    elif style in ["box", "line_box", "box_hang"]:
        marker_first = "╭"
        marker_middle = "├"
        marker_last = "╰"

        # Here we need a fancy title to go with the box
        if title:
            marker_first = marker_middle
            title = boxtitle(title, style="hang", return_str=True)
    else:
        marker_first = style
        marker_middle = style
        marker_last = style

    return marker_first, marker_middle, marker_last, title


def decide_marker(idx, marker_first, marker_middle, marker_last, style, data):

    if idx == 0:
        marker = marker_first

    elif idx == len(data) - 1:
        marker = marker_last

    else:
        marker = marker_middle

    # In case ordinal list, override marker
    if style in ["ordinal", "#", "numbered", "num"]:
        maxdigits = len(str(len(data))) + 1
        marker = f"{int(idx+1)}.".zfill(maxdigits)

    return marker


def hsv2rgb(hsv_tuple):

    """Converts HSV floats to 8-bit RGB."""
    h = hsv_tuple[0]
    s = hsv_tuple[1]
    v = hsv_tuple[2]

    rgb_tuple = tuple(int(round(i * 255)) for i in colorsys.hsv_to_rgb(h, s, v))

    return rgb_tuple


def rgb2hsv(rgb_tuple):

    """Converts RGB floats to HSV."""
    r = rgb_tuple[0]
    g = rgb_tuple[1]
    b = rgb_tuple[2]

    hsv_tuple = colorsys.rgb_to_hsv(r, g, b)

    return hsv_tuple


def hex2rgb(hex_string):
    hex = hex_string.lstrip("#")

    rgb = []
    try:
        for i in (0, 2, 4):
            decimal = int(hex[i : i + 2], 16)
            rgb.append(decimal / 255)
    except:
        error_message = f"'{hex_string}' is not a valid hex color {emoji.sad}"
        raise ValueError(error_message)

    return tuple(rgb)


def parse_color(color, cmap):
    """Guess the color that the user wants

    Returns
    -------
    tuple
        HSV color tuple (ouf default format for colors).

    """
    default_saturation = 0.8

    if color == "random":
        color = (random(), default_saturation, 1)
    elif color in ["red", "r"]:
        color = (0.98, default_saturation, 1)
    elif color in ["orange", "o"]:
        color = (0.05, default_saturation, 1)
    elif color in ["yellow", "y"]:
        color = (0.14, default_saturation, 1)
    elif color in ["green", "g"]:
        color = (0.35, default_saturation, 1)
    elif color in ["cyan", "c", "aqua", "a"]:
        color = (0.5, default_saturation, 1)
    elif color in ["blue", "b"]:
        color = (0.58, default_saturation, 1)
    elif color in ["indigo", "i"]:
        color = (0.67, default_saturation, 1)
    elif color in ["violet", "v", "purple"]:
        color = (0.74, default_saturation, 1)
    elif color in ["magenta", "m", "pink", "p"]:
        color = (0.85, default_saturation, 1)
    elif color in ["gray", "grey"]:
        color = (0, 0, 0.7)
    elif color in ["black", "k"]:
        color = (0, 0, 0)
    elif color in ["white", "w"]:
        color = (0, 0, 1)

    elif "#" in str(color):
        color = rgb2hsv(hex2rgb(color))

    # In case a single float is given we use a color map
    if isinstance(color, float) and color >= 0 and color <= 1:
        original_value = color
        if cmap == "hsv":
            color = (color, default_saturation, 1)

        elif cmap == "green-red":
            color = rgb2hsv([color, 1 - color, 0])
            color = (color[0], default_saturation, 1)

        elif cmap == "blue-red":
            color = rgb2hsv([color, 0, 1 - color])
            color = (color[0], default_saturation, 1)

        elif cmap == "cool":
            color = rgb2hsv([color, 0.8 - color, 1])
            color = (color[0], default_saturation, 1)

        elif cmap == "hot":
            color = rgb2hsv([1, 0.8 - color, color / 2])
            color = (color[0], default_saturation, 1)

        elif cmap == "greys":
            color = (0, 0, color)

        elif cmap == "random":
            color = (random(), default_saturation, 1)

    return color
