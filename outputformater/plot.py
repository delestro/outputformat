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

    if style in ["block"]:
        start = ""
        fill = "▓"
        empty = "░"
        end = ""

    elif style in ["battery"]:
        start = "┫"
        fill = "█"
        empty = " "
        end = "┣"

    elif style in ["bar"]:
        start = "["
        fill = "■"
        empty = " "
        end = "]"

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
        # Use values given as a list
        if isinstance(style, list):
            start = str(style[0])
            fill = str(style[1])
            empty = str(style[2])
            end = str(style[3])
        # Just use the char given
        else:
            start = "["
            fill = str(style)
            empty = " " * len(str(style))
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
        outputstring += f" {value:>{len(str(maxvalue))}}/{maxvalue}"

    if show_percentage:
        outputstring += f" ({value/maxvalue:>7.2%})"

    if return_str:
        return outputstring
    else:
        print(outputstring)


def barlist(
    values,
    titles,
    maxvalue=False,
    style="circle",
    length=32,
    show_values=True,
    show_percentage=True,
    return_str=False,
):

    if len(values) != len(titles):
        errormsg = f"'values' and 'titles' mus have the same length {emoji.sad}"
        errormsg += f"\ntotal values: {len(values)}"
        errormsg += f"\ntotal titles: {len(titles)}"
        raise ValueError(errormsg)

    outputstring = ""

    # In case maxvalue is no given,
    # uses the max from all the values
    if not maxvalue:
        maxvalue = max(values)

    # Get the longest title to use the proper padding
    longest_title = len(max(titles, key=len))

    # Create each row
    for idx in range(len(values)):
        outputstring += bar(
            values[idx],
            maxvalue,
            style=style,
            title=titles[idx],
            title_pad=longest_title,
            length=length,
            show_values=show_values,
            show_percentage=show_percentage,
            return_str=True,
        )
        outputstring += "\n"

    if return_str:
        return outputstring
    else:
        print(outputstring)
