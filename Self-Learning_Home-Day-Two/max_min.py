def find_max_min(list_of_numbers):
    """
    A function to return the minimum and maximum number in a list
    and if the min and max are equal, return the number of elements in the list
    """

    # initialize array to hold answer values
    answer_array = []

    # Get maximum value from the input numbers list
    max_num = max(list_of_numbers)

    # Get minimum value from the input numbers list
    min_num = min(list_of_numbers)

    # Check to see if all array items similar
    if min_num == max_num:
        num_of_elements = len(list_of_numbers)
        answer_array.append(num_of_elements)
    else:
        # Append the min and max values to answer array
        answer_array.append(min_num)
        answer_array.append(max_num)

    return answer_array
