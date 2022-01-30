def br(nlines=1, return_str=False):
    """Short summary.

    Parameters
    ----------
    nlines : int
        Number of lines to break.
    return_str : bool
        If True, returns a string instead of printing.

    """

    outputstring = "\n" * (nlines - 1)

    if return_str:
        return outputstring
    else:
        print(outputstring)


def b(input, return_str=False):
    """Bold the string"""
    ansi_bold = "\033[1m"
    ansi_end = "\033[0m"

    outputstring = f"{ansi_bold}{str(input)}{ansi_end}"

    if return_str:
        return outputstring
    else:
        print(outputstring)
