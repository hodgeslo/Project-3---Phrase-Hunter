# Create your Phrase class logic here.
from phrasehunter import game

class Phrase:
    def __init__(self, phrase):
        self.active_phrase = phrase.lower()
        self.active_phrase_list = list(self.active_phrase)

    def __str__(self):
        return self.active_phrase

    def __iter__(self):
        return iter(self.active_phrase)

    """
     TODO: display(): this prints out the phrase to the console with guessed letters visible and unguessed letters as 
     underscores. For example, if the current phrase is "hello world" and the user has guessed the letter "o", 
     the output should look like this: _ _ _ _ o   _ o _ _ _ 
    """

    def display(self, user_guessed_list):
        # print(f"from phrase.display() WHAT: {user_guessed_list}")

        # print(f"\nACTIVE PHRASE LIST: {list(self.active_phrase)}")

        dashed_list = []

        for key, value in enumerate(iter(self.active_phrase)):
            if value.isalpha():
                value = "_"
                dashed_list.append(value)
            else:
                value = " "
                dashed_list.append(value)

        for a, b in enumerate(user_guessed_list):
            for idx, itm in enumerate(self.active_phrase):
                if itm == b:
                    dashed_list[idx] = itm
        print(f"\n {' '.join(dashed_list)}")

        phrase_complete = self.check_complete(dashed_list)

        return phrase_complete

    """
    TODO: checks to see if the letter selected by the user matches a letter in the phrase.
    """

    def check_letter(self, user_guess_character):
        if user_guess_character in list(self.active_phrase):
            return True
        else:
            return False

    """
    TODO: checks to see if the whole phrase has been guessed
    """

    def check_complete(self, user_guessed_list):
        if user_guessed_list.count("_") > 0:
            print("game in progress")
        else:
            # print(f"you win!")
            return "You win!!!!"
