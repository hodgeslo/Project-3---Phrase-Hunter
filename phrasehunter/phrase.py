# Create your Phrase class logic here.
class Phrase:
    def __init__(self, phrase):

        self.phrase = phrase
        print(f"FROM class Phrase:  {self.phrase}") # remove later
        for word in self.phrase:
            print(word)

    """
     TODO: display(): this prints out the phrase to the console with guessed letters visibile and unguessed letters as 
     underscores. For example, if the current phrase is "hello world" and the user has guessed the letter "o", 
     the output should look like this: _ _ _ _ o   _ o _ _ _ 
    """

    def display(self):
        pass

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
