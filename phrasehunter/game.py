# Create your Game class logic in here.
from phrasehunter import phrase
import random
class Game:

    def __init__(self):
        """
        missed: used to track the number of incorrect guesses by the user. The initial value is 0 since no guesses
        have been made at the start of the game.
        phrases: a list of five Phrase objects to use with the game. A
        phrase should only include letters and spaces -- no numbers, puntuation or other special characters.
        active_phrase: This is the Phrase object that's currently in play. The initial value will be None. Within the
        start() method, this property will be set to the Phrase object returned from a call to the get_random_phrase(
        ) method. guesses: This is a list that contains the letters guessed by the user.
        """
        self.missed = 0
        self.phrases = [
            "JAWS OF DEATH",
            "HANDS DOWN",
            "LICKETY SPLIT",
            "GREASED LIGHTNING",
            "QUICK ON THE DRAW",
            "A BUSY BEE",
            "CUT THE MUSTARD",
            "CAT IN THE HAT",
            "BREAK THE ICE",
            "A HAIR’S BREADTH"
        ]
        self.active_phrase = None
        self.guesses = []
        self.active_game = True



    """
    Calls the welcome method, creates the game loop, calls the get_guess method, adds the user's guess to guesses, 
    increments the number of missed by one if the guess is incorrect, calls the game_over method.
    thephrase = phrase.RandomPhrase()
    print(thephrase)
    phrase.Phrase(thephrase)
    """
    def start(self):
        self.get_random_phrase()
        print(f"From start() random phrase: {self.active_phrase}") # remove later

        # display welcome message to player
        self.welcome()

        phrase.Phrase(self.active_phrase)

        while self.active_game:
            self.get_guess()



    """
     get_random_phrase(): this method randomly retrieves one of the phrases stored in the phrases list and returns it.
    """
    def get_random_phrase(self):
        self.random_phrase_index = random.randrange(0, 10)
        self.active_phrase = self.phrases[self.random_phrase_index]
        return self.active_phrase


    """
    welcome(): this method prints a friendly welcome message to the user at the start of the game
    """
    def welcome(self):
        print(f"WELCOME TO PHRASE HUNTER")


    """
    get_guess(): this method gets the guess from a user and records it in the guesses attribute
    """
    def get_guess(self):
        print("\nGET GUESS")
        user_guess = input("Guess a letter:  ").lower()
        if user_guess == "" or not user_guess.isalpha() or len(user_guess) > 1:
            print(f"Invalid entry. Enter a letter.")
        else:
            self.guesses.append(user_guess)
            phrase.Phrase.check_letter(user_guess, self.guesses, self.active_phrase)
        print(self.guesses)



    """
    game_over(): this method displays a friendly win or loss message and ends the game.
    """
    def game_over(self):
        pass