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
        ) method.
        guesses: This is a list that contains the letters guessed by the user.
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
            "A HAIR LENGTH"
        ]
        self.active_phrase = None
        self.guesses = []

    """
     get_random_phrase(): this method randomly retrieves one of the phrases stored in the phrases list and returns it.
    """

    def get_random_phrase(self):
        return random.choice(self.phrases)

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

        if not self.guesses:
            # print(f"NOT EMPTY:  self.guesses []")
            for key, value in enumerate(self.active_phrase):
                # print(key, value)
                if value.isalpha():
                    value = "_"
                    print("_", end=" ")
                    # dashed_list.append(value)
                    # print(f"TEMP LIST: {temp_list}")
                else:
                    value = " "
                    print("  ", end="")
                    # dashed_list.append(value)

        user_guess = input("\n\nGuess a letter:  ").lower()

        if user_guess == "" or not user_guess.isalpha() or len(user_guess) > 1 or [idx for idx, element in enumerate(self.guesses) if element == user_guess]:
            print(f"Invalid entry or you already guessed that letter. Enter a letter and ensure that it is not a duplicate guess.")
        else:
            if self.active_phrase.check_letter(user_guess) is False:
                print(f"FALSE FOOL")
                self.missed += 1
                print(self.missed)
                # self.active_phrase.display()
            else:
                print(f"TRUE TRAMP")
                self.guesses.append(user_guess)
                # print(f"from true tramp:  {self.active_phrase.display(user_guess)}")
                # self.active_phrase.display(user_guess)
                self.active_phrase.display(self.guesses)
                # print(f"from true tramp:  {self.active_phrase.display(self.guesses)}")
        # print(f"user guesses matched:  {self.guesses}")

    """
    game_over(): this method displays a friendly win or loss message and ends the game.
    """

    def game_over(self):
        return f"GAME OVER"

    """
    Calls the welcome method, creates the game loop, calls the get_guess method, adds the user's guess to guesses, 
    increments the number of missed by one if the guess is incorrect, calls the game_over method.
    """

    def start(self):
        # display welcome message to player
        self.welcome()

        # print(f"from start() with initial value: {self.active_phrase} and {id(self.active_phrase)}")

        self.active_phrase = phrase.Phrase(self.get_random_phrase())

        print(f"From start(): {self.active_phrase} and {id(self.active_phrase)}")  # remove later

        # for key, value in enumerate(self.active_phrase):
        #     if value.isalpha():
        #         print("_", end=" ")
        #     else:
        #         print("  ", end="")

        while self.missed < 5:
            self.get_guess()
        else:
            print(self.game_over())
