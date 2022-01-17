from outputformat.title import boxtitle
from outputformat.title import linetitle
from outputformat import tools


def showlist(data, style="bullet", title=False, return_str=False, precision=4):
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

    # Prepare and clean data
    data = tools.prepare_data(data, precision=precision)

    # Get markers and title
    markers = tools.get_markers_and_title(style, title)
    marker_first, marker_middle, marker_last, title = markers

    # Add title, if we have one
    if title:
        outputstring += f"{title}\n"

    # Add list items
    for idx in range(len(data)):

        marker = tools.decide_marker(
            idx, marker_first, marker_middle, marker_last, style, data
        )

        # Generate string for this item
        outputstring += f"{marker} {data[idx]}\n"

    if return_str:
        return outputstring
    else:
        print(outputstring)
