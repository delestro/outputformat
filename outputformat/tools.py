from outputformat.title import linetitle
from outputformat.title import boxtitle


def prepare_data(input_data, precision):
    """
    Prepare the input data so that display is cleaner
    """

    data = input_data.copy()

    # Check if we have negative and positive values
    # If we don't have negative values, there's no point in adding "+"
    # To align the list
    negative_values = False
    for value in data:
        if isinstance(value, (int, float)) and value < 0:
            negative_values = True

    for idx, value in enumerate(data):

        # In case float, adjust precision
        if isinstance(value, float):
            data[idx] = f"{value:.{precision}f}"
            if negative_values and value > 0:
                data[idx] = "+" + data[idx]

        # In case int, just add "+" if needed
        if isinstance(value, int):
            data[idx] = f"{value}"
            if negative_values and value > 0:
                data[idx] = "+" + data[idx]

        # In case list, be recursive
        if isinstance(value, list):
            data[idx] = prepare_data(value, precision=precision)

    return data


def get_markers_and_title(style, title=False):

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

    return marker_first, marker_middle, marker_last, title


def decide_marker(idx, marker_first, marker_middle, marker_last, style, data):

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

    return marker
