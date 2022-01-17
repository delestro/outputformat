from outputformat.title import boxtitle
from outputformat.title import linetitle
from outputformat import tools


def showdict(data, style="line", title=False, return_str=False, precision=4):
    # Start outputstring
    outputstring = ""

    # Get keys and values as lists
    keys = list(data.keys())
    values = list(data.values())

    # Clean values
    values = tools.prepare_data(values, precision=precision)

    # Get the longest title to use the proper padding
    longest_key = len(max(keys, key=len))

    # Get markers and title
    markers = tools.get_markers_and_title(style, title)
    marker_first, marker_middle, marker_last, title = markers

    if title:
        outputstring += title + "\n"

    for idx in range(len(data)):

        marker = tools.decide_marker(
            idx, marker_first, marker_middle, marker_last, style, data
        )

        # Get value to display
        value = values[idx]

        # In case value is a list, fix display
        if isinstance(value, list):
            clean_value = ""
            for idx, sub_value in enumerate(value):
                clean_value += f"{sub_value}"
                if idx < len(value) - 1:
                    clean_value += ", "

            value = clean_value

        # Add to the outputstring
        outputstring += f"{marker} {keys[idx]:.<{longest_key}}: {value}"
        outputstring += "\n"

    if return_str:
        return outputstring
    else:
        print(outputstring)
