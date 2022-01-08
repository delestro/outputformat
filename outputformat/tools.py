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

        if isinstance(value, float):
            data[idx] = f"{value:.{precision}f}"
            if negative_values and value > 0:
                data[idx] = "+" + data[idx]

        if isinstance(value, int):
            data[idx] = f"{value}"
            if negative_values and value > 0:
                data[idx] = "+" + data[idx]

    return data
