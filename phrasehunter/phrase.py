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
        print(f"from phrase.display():  {self.active_phrase} and {id(self.active_phrase)}")
        print(f"from phrase.display(): {user_guess}")

        temp_list = []
        for idx, val in enumerate(self.active_phrase):
            temp_list.append(val)
        print(temp_list)

        for key, value in enumerate(self.active_phrase):
           # print(key, value)
            if value.isalpha():
                print("_", end=" ")
                temp_list.append(value)
                # print(f"TEMP LIST: {temp_list}")
            else:
                print("  ", end="")
                temp_list.append(value)

        print(f"TEMP LIST: {temp_list}")

        # temp_list = [user_guess if item == user_guess else item for item in temp_list]

        # print(temp_list)


    """
    TODO: checks to see if the letter selected by the user matches a letter in the phrase.
    """

    def check_letter(self, user_guess):
        print(f"DEEZ NUTS")
        print(f"what is this CLASS: {self.__str__()} and {type(self)}")
        print(f"what is this: {user_guess}")
        print(f"from check letter:  {self.active_phrase} and {id(self.active_phrase)} and {type(self.active_phrase)}")
        if self.__str__().find(user_guess) ==  -1:
            return False
        elif self.__str__().find(user_guess) >= 0:
            return True

    """
    TODO: checks to see if the whole phrase has been guessed
    """

    def check_complete(self):
        pass
