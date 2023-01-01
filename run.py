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
        self.board = [["." for x in range(board_size)] for y in range(board_size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print_board(self):
        for row in self.board:
            print(" ".join(row))
    
    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"
        if (x,y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Missed"



#data = GameBoard(5, 4, "Marcos", type="player")
#guess = data.guess(1, 2)
#print(guess)
#print(data.print_board())