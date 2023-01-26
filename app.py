# Import your Game class

# Create your Dunder Main statement.

# Inside Dunder Main:
# Create an instance of your Game class
# Start your game by calling the instance method that starts the game loop
from phrasehunter import game

# if __name__ == '__main__':
#     games = game.Game()
#     games.start()
#     if not games.game_over():
#         print("THE GAME IS OVER")
#     else:
#         games = game.Game()
#         games.start()


if __name__ == '__main__':
    games = game.Game()
    games.start()
