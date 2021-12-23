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
