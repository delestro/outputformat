from outputformater import fonts


def boxtitle(txt, style="-", return_str=False):

    txt = str(txt)
    txt_size = len(txt)
    style = str(style)

    if style in ["-", "|", "line"]:
        lh = "─"
        lv = "│"
        tl = "╭"
        tr = "╮"
        bl = "╰"
        br = "╯"
    elif style in ["=", "||", "double"]:
        lh = "═"
        lv = "║"
        tl = "╔"
        tr = "╗"
        bl = "╚"
        br = "╝"

    elif style in ["--", ".", "..", ":", "dots"]:
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

    # Get the font_dict ot be used
    font_dict = getattr(fonts, style)

    # Make sure it's a string an lowercase it
    txt = str(txt).lower()

    # Check if we can print the string
    for char in txt:
        if char not in [supported for supported in fonts.suported_chars]:
            error_message = (
                f"'{char}' is not supported by 'bigtitle' \U0001F625"
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
