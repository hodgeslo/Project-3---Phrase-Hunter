# Import your Game class

# Create your Dunder Main statement.

# Inside Dunder Main:
# Create an instance of your Game class
# Start your game by calling the instance method that starts the game loop
import logging
from phrasehunter import game

logging.basicConfig(filename='game.log', level=logging.DEBUG)

if __name__ == '__main__':
    games = game.Game()
    games.start()
    if not games.game_over():
        print("THE GAME IS OVER")
    else:
        games = game.Game()
        games.start()


# if __name__ == '__main__':
#     games = game.Game()
#     games.start()
