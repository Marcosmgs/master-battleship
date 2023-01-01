from random import randint

scores = {"computer": 0, "player": 0}


class GameBoard:
    """
    Main game class, sets the board size, number of ships, 
    players name and the game board type for computer or player
    Contains methods for adding ships, guesses, players inputs
    and printing board.
    """

    def __init__(self, board_size, num_ships, name, type):
        self.board_size = board_size
        self.board = ["." for x in range(board_size) for y in range(board_size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []
    
data = GameBoard(5, 4, "Marcos", type = "player")
print(data.board_size)