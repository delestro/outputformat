from outputformat.title import boxtitle
from outputformat.title import linetitle


def showlist(data, style="bullet", title=False, return_str=False):
    """Show each item of a given list.

    Parameters
    ----------
    data : list
        List of items to display. Anything passed here will be converted to list

    style : string, default: 'bullet'
        How items are displayed. Options are: 'bullet', 'line', 'box', 'ordinal'
        'bullet' or '*': Simple bullet points
        'line' or '-': Line under the title, connected to the items
        'box': Title with a box decoration
        'ordinal' or '#': Shows a numbered list in ascending order

        In case any other string is passed, it will be used as marker
        For example:
        >>> showlist(["Item A", "Item B", "Item C"], style="~>")
        ~> Item A
        ~> Item B
        ~> Item C

    title : string, optional
        Title to be displayed before the list.
        In case 'title = False', the 'line' and 'box' styles give the same result

    return_str : Bool, default: False
        If True, returns a string instead of printing.

    Returns
    -------
    string
        Only returns in case 'return_str = True', otherwise None

    """

    # Start outputstring
    outputstring = ""

    # Make sure we have a list
    data = list(data)

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

    # Add title, if we have one
    if title:
        outputstring += f"{title}\n"

    # Add list items
    for idx in range(len(data)):

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

        # Generate string for this item
        outputstring += f"{marker} {data[idx]}\n"

    if return_str:
        return outputstring
    else:
        print(outputstring)
