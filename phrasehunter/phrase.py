# Create your Phrase class logic here.
from phrasehunter import game

class Phrase:
    def __init__(self, phrase):
        self.active_phrase = phrase.lower()
        print(f"FROM class Phrase:  {self.active_phrase}") # remove later
        self.display()
        # for word in self.active_phrase:
        #     print(word)

    """
     TODO: display(): this prints out the phrase to the console with guessed letters visibile and unguessed letters as 
     underscores. For example, if the current phrase is "hello world" and the user has guessed the letter "o", 
     the output should look like this: _ _ _ _ o   _ o _ _ _ 
    """

    def display(self):
        print(f"from Prase.display(): {self.active_phrase}")
        print(len(self.active_phrase))

        for key, value in enumerate(self.active_phrase):
            if value.isalpha():
                print("_", end=" ")
            else:
                print("  ", end="")

    """
    TODO: checks to see if the letter selected by the user matches a letter in the phrase.
    """

    def check_letter(self):
        print(f"check_letter(): {self}")


    """
    TODO: checks to see if the whole phrase has been guessed
    """

    def check_complete(self):
        pass
