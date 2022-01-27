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
