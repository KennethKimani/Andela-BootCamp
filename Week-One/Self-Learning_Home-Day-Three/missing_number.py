def find_missing(array_one, array_two):
    """MissingNumberTest to compares two lists and return the extra number in the longer list"""

    # check if first array length is equal to the second array length
    if len(array_one) == len(array_two):
        extra_number = [0]
    else:

        # check if first array length is greater than second array length
        if len(array_one) > len(array_two):
            longer_list = array_one
            shorter_list = array_two

        # check if second array length is greater than first array length
        else:
            longer_list = array_two
            shorter_list = array_one

        # get the missing number by comparing the  longer_list and the shorter_list
        extra_number = [x for x in longer_list if x not in shorter_list]

    return extra_number.pop()
