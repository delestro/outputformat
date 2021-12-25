from outputformater import emoji


def bar(
    value,
    maxvalue,
    style="block",
    length=32,
    title=False,
    title_pad=0,
    show_values=True,
    show_percentage=True,
    return_str=False,
):

    # Check if value < maxvalue
    if value > maxvalue:
        raise ValueError(f"'value' cannot be bigger than 'maxvalue' {emoji.crazy}")

    elif style in ["block"]:
        start = ""
        fill = "▓"
        empty = "░"
        end = ""

    elif style in ["battery"]:
        start = "┫"
        fill = "█"
        empty = " "
        end = "┣"

    elif style in ["hatch"]:
        start = "│"
        fill = "🮙"
        empty = " "
        end = "│"

    elif style in ["circle"]:
        start = ""
        fill = "●"
        empty = "○"
        end = ""

    elif style in ["star"]:
        start = ""
        fill = f"{emoji.star}"
        empty = ""
        end = ""

    else:
        if isinstance(style, list):
            start = str(style[0])
            fill = str(style[1])
            empty = str(style[2])
            end = str(style[3])
        else:
            start = "["
            fill = str(style)
            empty = " "
            end = "]"

    ratio = value / maxvalue
    nfill = int(ratio * length)

    # Start outputstring
    outputstring = ""
    if title:
        title = str(title)

        outputstring += f"{title:.<{title_pad}}: "
    outputstring += start
    outputstring += f"{fill*nfill}{empty*(length-nfill)}"
    outputstring += end

    if show_values:
        outputstring += f" {value}/{maxvalue}"

    if show_percentage:
        outputstring += f" ({value/maxvalue:.2%})"
    if return_str:
        return outputstring
    else:
        print(outputstring)
