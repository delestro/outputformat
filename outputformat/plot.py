from outputformat import emoji


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
    """Generate a single bar using ASCII.

    Parameters
    ----------
    value : int, float
        The value, or height, of this bar.

    maxvalue : int, float
        The maxium value this variable shoud have.

    style : string
        Style of bar. Options are: 'block', 'battery', 'bar', 'circle', 'star'
        'block'.....: ▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░
        'battery'...: ┫████████████      ┣
        'bar'.......: [■■■■■■■■■■■■      ]
        'circle'....: ●●●●●●●●●●●●○○○○○○
        'star': uses the Unicode star emoji '\U00002B50'

        In case of using 'star', it is recommended a low value for 'length',
        usually something as 3 or 5 (interesting for ratings)

        An list of strings can also be passed, as:
        >>> bar(35, 50, style=["(", "X", "-", ")"], title="Custom style")
        Custom style: (XXXXXXXXXXXXXXXXXXXXXX----------) 35/50 ( 70.00%)

        The characters in the list are used to build the bar,
        and only the first 4 values in the list are used.

        If a single string character is passed, it is used for a basic bar:
        >>> bar(35, 50, style="$", title="Custom style")
        Custom style: [$$$$$$$$$$$$$$$$$$$$$$          ] 35/50 ( 70.00%)

    length : int
        Total size of the bar (in characters) to be displayed.

    title : string, optional
        Text for a title displayed before the bar.

    title_pad : int, optional
        Padding to the right of title. Usefull to aling several bars.

    show_values : Bool
        If True, shows the values as 'value/maxvalue' in front of the bar

    show_percentage : Bool
        If True, shows the percentage in front of the bar

    return_str : Bool, default: False
        If True, returns a string instead of printing.

    Returns
    -------
    string
        Only returns in case 'return_str = True', otherwise None


    """

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
    """Short summary.

    Parameters
    ----------
    values : list
        list of values to be displayed (paired with 'titles').

    titles : list
        list of titles to be displayed (paired with 'values').

    maxvalue : int, float, optional
        The max value that any of the 'values' could have.

        In case None (or False) is given, uses the max value from all the values

    style : string
        Style passed to outputformat.bar
        Options are: 'block', 'battery', 'bar', 'circle', 'star'
        'block'.....: ▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░
        'battery'...: ┫████████████      ┣
        'bar'.......: [■■■■■■■■■■■■      ]
        'circle'....: ●●●●●●●●●●●●○○○○○○
        'star': uses the Unicode star emoji '\U00002B50'
            In case of using 'star', it is recommended a low value for 'length',
            usually something as 3 or 5 (interesting for ratings)

        An list of strings can also be passed, as:
        >>> bar(35, 50, style=["(", "X", "-", ")"], title="Custom style")
        Custom style: (XXXXXXXXXXXXXXXXXXXXXX----------) 35/50 ( 70.00%)

        The characters in the list are used to build the bar,
        and only the first 4 values in the list are used.

        If a single string character is passed, it is used for a basic bar:
        >>> bar(35, 50, style="$", title="Custom style")
        Custom style: [$$$$$$$$$$$$$$$$$$$$$$          ] 35/50 ( 70.00%)



    length : int
        Total size of the bars, in characters.

    show_values : Bool
        If True, shows the values as 'value/maxvalue' in front of the bar

    show_percentage : Bool
        If True, shows the percentage in front of the bar

    return_str : Bool, default: False
        If True, returns a string instead of printing.

    Returns
    -------
    string
        Only returns in case 'return_str = True', otherwise None


    """

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
