from outputformat import fonts
from outputformat import emoji

# lh ➔ line horizontal
# lv ➔ line vertical
# tl ➔ top left
# tr ➔ top right
# bl ➔ bottom left
# br ➔ bottom right


def linetitle(txt, style="-", return_str=False):
    """Simple line under text.

    Parameters
    ----------
    txt : string
        Text to be displayed.

    style : string
        Style for the title. Options are: 'line', 'double', 'line_hang'
        'line' or '-': single line under text
        'double' or '=': double line under text
        'line_hang': simple line with a hanger

        If any other value is passed, it will be converted to string and
        used as character for the line. For example:

        >>> linetitle("Title with custom style", style="%")
        Title with custom style
        %%%%%%%%%%%%%%%%%%%%%%%

    return_str : Bool, default: False
        If True, returns a string instead of printing.

    Returns
    -------
    string
        Only returns in case 'return_str = True', otherwise None


    """
    # Start outputstring
    outputstring = ""

    txt = str(txt)
    txt_size = len(txt)
    style = str(style)

    # bl = bottom left
    # lh = line horizontal
    if style in ["line", "-"]:
        bl = "─"
        lh = "─"
        space = ""

    if style in ["=", "double"]:
        bl = "═"
        lh = "═"
        space = ""

    elif style in ["line_hang", "hanging", "hang"]:
        bl = "╭"
        lh = "─"
        space = " "
    else:
        bl = str(style)[0]
        lh = str(style)[0]
        space = ""

    # Build string
    outputstring += f"{space}{txt}\n"
    outputstring += f"{bl}{lh*(txt_size-1)}{lh*len(space)}"

    if return_str:
        return outputstring
    else:
        print(outputstring)


def boxtitle(txt, style="-", return_str=False):
    """Creates a text with a box decoration.

    Parameters
    ----------
    txt : string
        Text to be displayed.

    style : string
        Style of the box. Options are 'line', 'line_hang', 'double', 'dashes'
        'line' or '-': Simple box with rounded corners
        'line_hang': Box with hanger in the bottom-left corner
        'double': Double line box
        'dashes' or '--': Box with dashed line

        If any other value is passed, it will be converted to
        string and used as character for the box

    return_str : Bool, default: False
        If True, returns a string instead of printing.

    Returns
    -------
    string
        Only returns in case 'return_str = True', otherwise None

    """

    txt = str(txt)
    txt_size = len(txt)
    style = str(style)

    if style in ["line", "-"]:
        lh = "─"
        lv = "│"
        tl = "╭"
        tr = "╮"
        bl = "╰"
        br = "╯"
    elif style in ["line_hang", "hanging", "hang"]:
        lh = "─"
        lv = "│"
        tl = "╭"
        tr = "╮"
        bl = "├"
        br = "╯"

    elif style in ["double", "="]:
        lh = "═"
        lv = "║"
        tl = "╔"
        tr = "╗"
        bl = "╚"
        br = "╝"

    elif style in ["dashes", "--", ".", "..", ":", "dots"]:
        lh = "╌"
        lv = "┊"
        tl = "╭"
        tr = "╮"
        bl = "╰"
        br = "╯"
    else:
        # Just use the first value of the provided string
        lh = lv = tl = tr = bl = br = style[0]

    # Build string
    outputstring = (
        (tl + (lh * (txt_size + 2) + tr))
        + "\n"
        + (lv + " " + txt + " " + lv)
        + "\n"
        + (bl + (lh * (txt_size + 2) + br))
    )

    if return_str:
        return outputstring
    else:
        print(outputstring)


def bigtitle(txt, style="small", return_str=False):
    """uses ASCII art to generate a big title.

    Parameters
    ----------
    txt : string
        Text to be displayed.
    style : string
        Style used for the ASCII art, for the moment, only 'small' is supported

        Fonts are defined in outputformat.fonts.py

        Supported chars are: 0123456789abcdefghijklmnopqrstuvwxyz_-!.'

    return_str : Bool, default: False
        If True, returns a string instead of printing.

    Returns
    -------
    string
        Only returns in case 'return_str = True', otherwise None

    """

    # Get the font_dict ot be used
    if style not in fonts.font_styles:
        error_message = (
            f"'{style}' is not supported by 'bigtitle' {emoji.sad}"
            + f"\nSupported styles: {fonts.font_styles}"
        )
        raise ValueError(error_message)

    font_dict = getattr(fonts, style)

    # Make sure it's a string an lowercase it
    txt = str(txt).lower()

    # Check if we can print the string
    for char in txt:
        if char not in [supported for supported in fonts.suported_chars]:
            error_message = (
                f"'{char}' is not supported by 'bigtitle' {emoji.sad}"
                + f"\nSupported chars: {fonts.suported_chars}"
            )
            raise ValueError(error_message)

    # Make the title
    nrows = len(font_dict[fonts.suported_chars[0]])
    outputstring = ""
    for row in range(nrows):
        for letter in txt:
            outputstring += font_dict[letter][row]
            outputstring += " "
        outputstring += "\n"

    if return_str:
        return outputstring
    else:
        print(outputstring)
