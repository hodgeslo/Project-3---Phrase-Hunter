# Create your Phrase class logic here.


class Phrase:
    def __init__(self, phrase):
        self.active_phrase = phrase.lower()
        self.active_phrase_list = list(self.active_phrase)

    def __str__(self):
        return self.active_phrase

    def __iter__(self):
        return iter(self.active_phrase)

    def __repr__(self):
        return self

    def find_indices(self, list_to_check, item_to_find):
        indices = []
        for idx, value in enumerate(list_to_check):
            if value == item_to_find:
                indices.append(idx)
        return indices


    """
     TODO: display(): this prints out the phrase to the console with guessed letters visible and unguessed letters as 
     underscores. For example, if the current phrase is "hello world" and the user has guessed the letter "o", 
     the output should look like this: _ _ _ _ o   _ o _ _ _ 
    """

    def display(self, user_guessed_list):
        # print(f"from phrase.display():  {self.active_phrase} and {id(self.active_phrase)}")
        print(f"from phrase.display() WHAT: {user_guessed_list}")

        print(f"\nTEMP LIST: {self.active_phrase_list}")

        for a, b in enumerate(user_guessed_list):
            print(b)
            # the_indices = [idx for idx, element in enumerate(self.active_phrase_list) if element == user_guessed_list[a]]
            print(self.active_phrase_list.index(b))

        dashed_list = []

        for a, b in enumerate(user_guessed_list):
            print(self.find_indices(self.active_phrase_list, b))

        for key, value in enumerate(self.active_phrase_list):
            # print(key, value)
            if value.isalpha():
                value = "_"
                # print("_", end=" ")
                dashed_list.append(value)
                # print(f"TEMP LIST: {temp_list}")
            else:
                value = " "
                # print("  ", end="")
                dashed_list.append(value)

        print(f"dash list!: {' '.join(dashed_list)}  ")

        """ WORK ABOVE THIS LINE """

        # for key, value in enumerate(temp_list):
        #     # print(key, value)
        #     if value.isalpha():
        #         value = "_"
        #         # print("_", end=" ")
        #         dashed_list.append(value)
        #         # print(f"TEMP LIST: {temp_list}")
        #     else:
        #         value = " "
        #         # print("  ", end="")
        #         dashed_list.append(value)

        # print(f"dash list!: {' '.join(dashed_list)}  ")

        # the_indices = [idx for idx, element in enumerate(temp_list) if element == user_guessed_list]
        # print(f"from display() the indices: {the_indices} and {type(the_indices)}")
        # (print("\n\n"))
        #
        # for i, k in enumerate(the_indices):
        #     dashed_list[k] = user_guessed_list
        #
        # my_list = dashed_list.copy()
        # print(f"MY LIST:  {my_list}")
        #
        # print(f"updated dash list!: {' '.join(dashed_list)}  ")
        #
        # print("\nWILL THIS WORK????")
        # for x, y in enumerate(user_guessed_list):
        #     print(x, y)
        #     print([idx1 for idx1, element1 in enumerate(temp_list) if element1 == user_guessed_list[x]])


        # return my_list


    """
    TODO: checks to see if the letter selected by the user matches a letter in the phrase.
    """

    def check_letter(self, user_guess_character):
        if user_guess_character in self.active_phrase_list:
            return True
        else:
            return False

    """
    TODO: checks to see if the whole phrase has been guessed
    """

    def check_complete(self):
        pass
