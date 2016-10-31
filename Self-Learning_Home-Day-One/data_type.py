def data_type(data):

    if data is None:
        return 'no value'

    elif isinstance(data, str):
        return len(data)

    elif isinstance(data, bool):
        return data

    elif isinstance(data, int):
        if data < 100:
            return "less than 100"
        elif data == 100:
            return "equal to 100"
        else:
            return "more than 100"

    elif isinstance(data, list):
        if len(data) >= 3:
            return data[2]
        else:
            return None
