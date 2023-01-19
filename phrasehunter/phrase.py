# Create your Phrase class logic here.

class Phrase:
    def __init__(self, phrase):
        self.active_phrase = phrase.lower()

    def __str__(self):
        return self.active_phrase

    def __iter__(self):
        return iter(self.active_phrase)

    """
     TODO: display(): this prints out the phrase to the console with guessed letters visible and unguessed letters as 
     underscores. For example, if the current phrase is "hello world" and the user has guessed the letter "o", 
     the output should look like this: _ _ _ _ o   _ o _ _ _ 
    """

    def display(self):
        for key, value in enumerate(self.active_phrase):
            if value.isalpha():
                print("_", end=" ")
            else:
                print("  ", end="")

    """
    TODO: checks to see if the letter selected by the user matches a letter in the phrase.
    """

    def check_letter(self):
        pass

    """
    TODO: checks to see if the whole phrase has been guessed
    """

    def check_complete(self):
        pass
