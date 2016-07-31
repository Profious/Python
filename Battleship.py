"""
LOL GET REKT
Battleship style game.  It first asks you to pick a spot for you battleship, then asks you to guess
the enemy's location.  The enemy also shoots at the player each turn, and code is put into place as
to insure that neither the player nor the enemy shoot/place their battleships in a stop that doesn't
make sense
"""


from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

player_row = int(raw_input("What row do you want your battleship to be in?  Row: ")) - 1
player_col = int(raw_input("What column do you want your battleship to be in?  Column: ")) - 1

if player_row > 4 or player_col > 4 or player_col < 0 or player_row < 0:
    print "\nThat location is unavailable. Please pick another spot (from 1 to 5).\n"
    player_row = int(raw_input("What row do you want your battleship to be in?  Row: ")) - 1
    player_col = int(raw_input("What column do you want your battleship to be in?  Column: ")) - 1
    if player_row > 4 or player_col > 4 or player_col < 0 or player_row < 0:
        print "\nThat location is also unavailable. Your battleship has been placed on row 3, column 3.\n"
        player_row = 2
        player_col = 2

board[player_row][player_col] = "B"

if player_row == ship_row and player_col == ship_col:
    if ship_row >= 3:
        ship_row = ship_row -1
    else:
        ship_row = ship_row + 1


for turn in range(50):
    guess_row = int(raw_input("Guess Row: ")) - 1
    guess_col = int(raw_input("Guess Col: ")) - 1

    enemy_guess_row = random_row(board)
    enemy_guess_col = random_col(board)

    for x in range(10000):
        if board[enemy_guess_row][enemy_guess_col] != "O" or board[enemy_guess_row][enemy_guess_col] != "B":
            enemy_guess_row = random_row(board)
            enemy_guess_col = random_row(board)
        if enemy_guess_col == guess_col and enemy_guess_row == guess_row:
            enemy_guess_row = random_row(board)
            enemy_guess_col = random_row(board)
    board[enemy_guess_row][enemy_guess_col] = "Y"

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sank the enemy's battleship!"
        break

    else:

        if (guess_row not in range(5) or guess_col not in range(5)) or board[guess_row][guess_col] != "O":
            print "Oops, that spot's not available."
        else:
            print "You missed the enemy's battleship!"
            board[guess_row][guess_col] = "X"
        if guess_col == player_col and guess_row == player_row:
            board[guess_row][guess_col] = "B"
        print "Turn", turn + 1
        print " "
        print print_board(board)
        print " \n "

    if enemy_guess_col == player_col and enemy_guess_row == player_row:
        answer = raw_input("Game Over!\nWould you like to know the position of the enemy's ship?(Y/N): ")
        if answer.lower() == 'y':
            print "The enemy's battleship was on row " + str(ship_row + 1) + " and column " + str(ship_col + 1) + "."
            board[ship_row][ship_col] = "E"
            board[enemy_guess_row][enemy_guess_col] = "C"
            print print_board(board)
        break
        
