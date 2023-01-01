from random import randint

scores = {"computer": 0, "player": 0}


class GameBoard:
    """
    Main game class, sets the board size, number of ships, 
    player's name and the game board type for computer or player.
    Contains methods for adding ships, guesses, player's inputs
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
    
    def add_ships(self, x, y, type="computer"):
        if len(self.ships) >= self.num_ships:
            print("Error: You can not add more ships to the board!")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "@"




data = GameBoard(5, 4, "Marcos", type="computer")
guess = data.add_ships(1, 2, type="computer")
print(data.ships)
print(data.print_board())