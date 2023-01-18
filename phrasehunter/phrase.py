# Create your Phrase class logic here.
import phrasehunter.phrase
from phrasehunter import game

class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        print(f"FROM class Phrase:  {self.phrase}")  # remove later
        self.display()
        # self.check_letter()
        # for word in self.phrase:
        #     print(word)

    """
     TODO: display(): this prints out the phrase to the console with guessed letters visible and unguessed letters as 
     underscores. For example, if the current phrase is "hello world" and the user has guessed the letter "o", 
     the output should look like this: _ _ _ _ o   _ o _ _ _ 
    """

    def display(self):
        print(f"from Phrase.display(): {self.phrase}")
        print(len(self.phrase))

        for key, value in enumerate(self.phrase):
            if value.isalpha():
                print("_", end=" ")
            else:
                print("  ", end="")

    """
    TODO: checks to see if the letter selected by the user matches a letter in the phrase.
    """
    def check_letter(self, user_guesses, active_phrase):
        active_string = active_phrase.lower()

        print(f"\nfrom check_letter(): {self}")
        print(f"\nfrom check_letter(): {user_guesses}")
        print(f"\nfrom check_letter(): {active_string}")

        print(active_string.find(self))

    """
    TODO: checks to see if the whole phrase has been guessed
    """

    def check_complete(self):
        pass
