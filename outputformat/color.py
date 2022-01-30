import outputformat as ouf

# Just a shortcut for the ANSI end code
ansi_end = "\033[0;00m"

# list of possible color maps
cmaps = ["hsv", "blue-red", "green-red", "cool", "hot", "greys", "random"]


def ansi_hsv(hsv_tuple):
    """Creates a ANSI code from a HSV tuple

    Parameters
    ----------
    hsv_tuple : tuple
        HSV color, tuple of 3 float values.

    Returns
    -------
    string
        ANSI code with the color

    """

    rgb_tuple = ouf.tools.hsv2rgb(hsv_tuple)

    ansi_pre = f"\033[38;2;{rgb_tuple[0]};{rgb_tuple[1]};{rgb_tuple[2]}m"

    return ansi_pre


def string_hsv(input, hsv_tuple):
    """Apply HSV color to string"


    Parameters
    ----------
    input : str
        Text to be colored.
    hsv_tuple : tuple
        Tuple for HSV color (h ,s, v)

    Returns
    -------
    str
        String with the ANSI color

    """
    string = str(input)
    ansi_pre = ansi_hsv(hsv_tuple)
    ansi_post = ouf.color.ansi_end
    return f"{ansi_pre}{string}{ansi_post}"


def c(input, color, cmap="hsv", bold=False, return_str=False):

    string = str(input)
    outputstring = ""

    if color == "rainbow":
        outputstring = ouf.rainbow(input, cmap=cmap, bold=bold, return_str=True)

    else:
        # Parse color
        color = ouf.tools.parse_color(color, cmap)
        outputstring = string_hsv(string, color)

        if bold:
            outputstring = ouf.b(outputstring, return_str=True)

    if return_str:
        return outputstring
    else:
        print(outputstring)


def rainbow(input, cmap="hsv", bold=False, return_str=False):
    string = str(input)

    outputstring = ""

    for idx, char in enumerate(string):
        ratio = idx / len(string)
        outputstring += ouf.c(char, color=ratio, cmap=cmap, bold=bold, return_str=True)

    if return_str:
        return outputstring
    else:
        print(outputstring)
