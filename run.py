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
        self.guesses = [(1,2)]
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

    def get_user_input(self):
        try:
            x_row = input("Enter the row of the ship: \n")
            while int(x_row) > self.board_size - 1:
                print("You Must Enter a Number between 0 and 4! \n")
                x_row = input("Enter the row of the ship: \n")

            y_col = input("Enter the column of the ship: \n")
            while int(y_col) > self.board_size - 1:
                print("You Must Enter a Number between 0 and 4!")
                y_col = input("Enter the column of the ship: \n")
            guess = (int(x_row), int(y_col))
            if guess not in self.guesses:
                return int(x_row), int(y_col)
            else:
                print("You already guessed this coordinates!")
                return self.get_user_input()
        except ValueError:
            print("Not valid input, please reenter coordinates.")
            return self.get_user_input()




#data = GameBoard(5, 4, "Marcos", type="computer")
#x, y = data.get_user_input()
#print(x, y)
