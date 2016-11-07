def words(input):
    """
            Counts the occurrences or characters in a word
        """
    # initialize an empty dictionary to hold the final answer
    collection = {}

    if type(input) == str:

        # split the input phrase to individual words
        split_phrase = input.split()

        for i in split_phrase:

            if i in collection:
            # already exists in our dictionary

                #make dictionary convert integer string to integer
                if i.isdigit() == True:
                    i = int(i)

                    # increment value by one if they exist
                    collection[i] += 1

                else: #treat it as a string


                    # increment value by one if they exist
                    collection[i] += 1

            else:
            #does not exist in our dictionary

                 # if key is a integer
                if i.isdigit() == True:
                    i = int(i)
                    collection[i] = 1
                else:
                    collection[i] = 1

        # return populated dictionary
        return collection
