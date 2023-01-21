# Create your Phrase class logic here.


class Phrase:
    def __init__(self, phrase):
        self.active_phrase = phrase.lower()

    def __str__(self):
        return self.active_phrase

    def __iter__(self):
        return iter(self.active_phrase)

    def __repr__(self):
        return self

    """
     TODO: display(): this prints out the phrase to the console with guessed letters visible and unguessed letters as 
     underscores. For example, if the current phrase is "hello world" and the user has guessed the letter "o", 
     the output should look like this: _ _ _ _ o   _ o _ _ _ 
    """

    def display(self, user_guess):
        show_initial_menu = True
        print(f"from phrase.display():  {self.active_phrase} and {id(self.active_phrase)}")
        print(f"from phrase.display(): {user_guess}")

        dashed_list = []
        temp_list = list(self.active_phrase)
        print(f"\nTEMP LIST: {temp_list}")

        for key, value in enumerate(self.active_phrase):
            print(key, value)
            if value.isalpha():
                value = "_"
                # print("_", end=" ")
                dashed_list.append(value)
                # print(f"TEMP LIST: {temp_list}")
            else:
                value = " "
                # print("  ", end="")
                dashed_list.append(value)
        # pprint blanks at start of game
        print(f"dash list!: {' '.join(dashed_list)}  ")

        the_indices = [idx for idx, element in enumerate(temp_list) if element == user_guess]
        print(f"from display() the indices: {the_indices} and {type(the_indices)}")
        (print("\n\n"))

        for i, k in enumerate(the_indices):
            dashed_list[k] = user_guess

        my_list = dashed_list.copy()
        print(f"MY LIST:  {my_list}")

        print(f"updated dash list!: {' '.join(dashed_list)}  ")


    """
    TODO: checks to see if the letter selected by the user matches a letter in the phrase.
    """

    def check_letter(self, user_guess):
        print(f"DEEZ NUTS")
        print(f"what is this CLASS: {self.__str__()} and {type(self)}")
        print(f"what is this: {user_guess}")
        print(f"from check letter:  {self.active_phrase} and {id(self.active_phrase)} and {type(self.active_phrase)}")
        if self.__str__().find(user_guess) == -1:
            return False
        elif self.__str__().find(user_guess) >= 0:
            return True

    """
    TODO: checks to see if the whole phrase has been guessed
    """

    def check_complete(self):
        pass
