# Create your Game class logic in here.
import logging

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
        self.max_num_of_attempts = 5
        self.phrases = [
            phrase.Phrase("JAWS OF DEATH"),
            phrase.Phrase("HANDS DOWN"),
            phrase.Phrase("LICKETY SPLIT"),
            phrase.Phrase("GREASED LIGHTNING"),
            phrase.Phrase("QUICK ON THE DRAW"),
            phrase.Phrase("A BUSY BEE"),
            phrase.Phrase("CUT THE MUSTARD"),
            phrase.Phrase("CAT IN THE HAT"),
            phrase.Phrase("BREAK THE ICE"),
            phrase.Phrase("A HAIR LENGTH")
        ]
        self.active_phrase = None
        self.guesses = []
        self.game_state = None
        self.active_game = None

    """
     get_random_phrase(): this method randomly retrieves one of the phrases stored in the phrases list and returns it.
    """

    def get_random_phrase(self):
        return random.choice(self.phrases)

    """
    welcome(): this method prints a friendly welcome message to the user at the start of the game
    """

    def welcome(self):
        print(r"""

  _____  _                          _    _             _              _____           _     _____ _____ 
 |  __ \| |                        | |  | |           | |            |  __ \         | |   |_   _|_   _|
 | |__) | |__  _ __ __ _ ___  ___  | |__| |_   _ _ __ | |_ ___ _ __  | |__) |_ _ _ __| |_    | |   | |  
 |  ___/| '_ \| '__/ _` / __|/ _ \ |  __  | | | | '_ \| __/ _ \ '__| |  ___/ _` | '__| __|   | |   | |  
 | |    \  __/ | |  | | |_| | | | | ||  __/ |    | |  | (_| | |  | |_   _| |_ _| |_  |  \   _| |_ _| |_
 |_|    |_| |_|_|  \__,_|___/\___| |_|  |_|\__,_|_| |_|\__\___|_|    |_|   \__,_|_|   \__| |_____|_____|
        """)
        print(f"The ultimate word guessing game. Can you guess the phrase without any misses?")
        print(f"You will be presented with a phrase that is masked by an underscore (_) for each letter of the word.")
        print(f"You have a limited number of times to guess incorrectly. Choose wisely your guesses.")
        print(f"Each guess should be one letter from A to Z.\n\n")

    """
    get_guess(): this method gets the guess from a user and records it in the guesses attribute
    """

    def get_guess(self):
        # print(f"from get_guess(): {self.active_phrase}")
        user_guess = input("\nGuess a letter:  ").lower()
        return user_guess

    """
    game_over(): this method displays a friendly win or loss message and ends the game.
    """

    def game_over(self):
        if self.game_state is "WIN":
            print("YOU WON")
            self.new_game()
        elif self.game_state is "LOSE":
            print("YOU LOST")
            self.new_game()


    def new_game(self):
        user_play_again = input("Would you like to play again? y/n  ")
        if user_play_again == " " or not user_play_again.isalpha():
            print(f"Oops, try again")
        elif user_play_again.lower() == 'y':
            self.active_game = True
            self.missed = 0
            self.guesses = []
            self.game_state = None
            self.active_phrase = self.get_random_phrase()
        elif user_play_again.lower() == 'n':
            print(f"Thanks for playing!")

    """
    Calls the welcome method, creates the game loop, calls the get_guess method, adds the user's guess to guesses, 
    increments the number of missed by one if the guess is incorrect, calls the game_over method.
    """

    def start(self):
        # display welcome message to player
        self.welcome()

        # print(f"from start() with initial value: {self.active_phrase} and {id(self.active_phrase)}")

        self.active_phrase = self.get_random_phrase()

        self.active_game = True

        while self.active_game:
            print(f"from start(): {self.active_phrase}")

            if not self.guesses:
                for key, value in enumerate(self.active_phrase):
                    if value.isalpha():
                        print("_", end=" ")
                    else:
                        print(" ", end=" ")

            user_guess = self.get_guess()

            if user_guess == "" or not user_guess.isalpha():
                print(f"*** Invalid entry. Enter one letter only between A and Z. ***")
            elif len(user_guess) > 1:
                print(f"*** Too many letters entered. Enter one letter only between A and Z. Try again! ***")
            elif [idx for idx, element in enumerate(self.guesses) if element == user_guess]:
                print(f"*** You already guessed that letter. Try again! ***")
            else:
                if self.active_phrase.check_letter(user_guess) is False:
                    self.missed += 1
                    print(f"\nYou have {self.max_num_of_attempts - self.missed} out of {self.max_num_of_attempts} lives remaining!\n")
                    if self.missed == 5:
                        self.active_game = False
                        self.game_state = "LOSE"
                        self.game_over()
                else:
                    self.guesses.append(user_guess)
                    if self.active_phrase.display(self.guesses):
                        self.active_game = False
                        self.game_state = "WIN"
                        self.game_over()
