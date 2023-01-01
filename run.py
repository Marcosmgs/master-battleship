from random import randint

scores = {"computer": 0, "player": 0}


class GameBoard:
    """
    Main game class, sets the board size, number of ships, 
    player's name and the game board type for computer or player.
    Contains methods for adding ships, guesses, player's inputs
    and printing board.
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
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
        if (x, y) in self.ships:
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
            while int(x_row) > self.size - 1:
                print("You Must Enter a Number between 0 and 4! \n")
                x_row = input("Enter the row of the ship: \n")

            y_col = input("Enter the column of the ship: \n")
            while int(y_col) > self.size - 1:
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

def random_num(size):
    """
    Helper function to every time its called,
    generates a random number between 0 and the board size
    """

    return randint(0, size -1)

def populate_board(board):
    """
    Randomnly populate ships on the boards instances
    """

    x = random_num(board.size)
    y = random_num(board.size)
    board.add_ships(x, y)

def guess_maker(board):
    """
    Process all the guesses and return the results, if it is a computer guess it generates randomnly
    and if it is a user guess, will get user input method to generats a valid guess.
    """
    
    if board.type == "player":
        x = random_num(board.size)
        y = random_num(board.size)
        computer_result = board.guess(x, y)
        print(f"Computer guesses: {(x, y)}")
        print(f"Computer {computer_result} this round")
    else:
        if board.type == "computer":
            x, y = board.get_user_input()
            player_result = board.guess(int(x), int(y))
            print(f"Player guesses: {(int(x), int(y))}")
            print(f"Player {player_result} this round!")
        return player_result

    return computer_result

def play_game(player_game, computer_game):
    """
    Runs the game and increment scores util user tell otherwise
    """

    keep_on = True
    while keep_on:
        print(f"{player_game.name}'s Board:")
        player_game.print_board()
        print()
        print("---------- VS ----------")
        print()
        print("Computer's Board:")
        computer_game.print_board()

        player_results = guess_maker(computer_game)
        computer_results = guess_maker(player_game)
        
        print("=" * 20)
        if player_results == "Hit":
            scores["player"] += 1
        else:
            if computer_results == "Hit":
                scores["computer"] += 1
        print(f"The Scores Are:")
        print(f"Computer: {scores['computer']} {player_game.name}: {scores['player']}")
        print("=" * 20)

        keep_playing = input("Type any input to keep play or N to quit game! \n")
        if keep_playing.lower() == "n":
            print("Now closing the game...")
            keep_on = False
        else:
            print("You have decided to play another round...")
    print("Thanks for playing")

def start_game():
    """
    Start the game every time it is called reseting scores. Sets size, number of ships
    and alocate it on the boards for a new game.
    """

    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print("#" * 35)
    print("    Battleship Master Challenge")
    print(f"  Board Size: {size} Number of ships: {num_ships}")
    print("  Top left corner is row: 0 col: 0")
    print("#" * 35)
    print("_" * 35)
    name = input("Please enter your name: \n")
    print("_" * 35)

    computer_game = GameBoard(size, num_ships, "computer", type="computer")
    player_game = GameBoard(size, num_ships, name, type="player")

    for _ in range(num_ships):
        populate_board(player_game)
        populate_board(computer_game)

    play_game(player_game, computer_game)

start_game()