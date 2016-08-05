"""
Battleship style game.  It first asks you to pick a spot for you battleship, then asks you to guess
the enemy's location.  The enemy also shoots at the player each turn, and code is put into place as
to insure that neither the player nor the enemy shoot/place their battleships in a stop that doesn't
make sense
"""


from random import randint


board = []
#THIS SETS THE BOARD
for x in range(0, 5):
    board.append(["O"] * 5)
#THIS IS WHAT'S USED EVERY TIME THE BOARD IS PRINTED
def print_board(board):
    for row in board:
        print " ".join(row)
#PICKS A RANDOM ROW
def random_row(board):
    return randint(0, len(board) - 1)
#PICKS A RANDOM COLUMN
def random_col(board):
    return randint(0, len(board) - 1)

#MAKES SURE THE ROW PICKED FOR THE PLAYER'S BATTLESHIP IS VALID
while True:
    try:
        player_row = int(raw_input("What row do you want your battleship to be in?  Row: ")) - 1
        useless_var_row = board[player_row]
        break
    except:
        print "\nThat location is unavailable. Please pick another row (from 1 to 5)."
#MAKES SURE THE COLUMN PICKED FOR THE PLAYER'S BATTLESHIP IS VALID
while True:
    try:
        player_col = int(raw_input("What column do you want your battleship to be in?  Column: ")) - 1
        useless_var_col = board[player_col]
        break
    except:
        print "\nThat location is unavailable. Please pick another column (from 1 to 5)."

board[player_row][player_col] = "B"

#PICKS THE ENEMY SHIP'S LOCATION
ship_row = random_row(board)
ship_col = random_col(board)

#ENSURES THAT BOTH SHIPS AREN'T IN THE SAME PLACE
while True:
    if player_row == ship_row and player_col == ship_col:
        ship_row = random_row(board)
        ship_col = random_col(board)
    else:
        break

#THE TURN SYSTEM
for turn in range(50):
    while True:
        try:
            guess_row = int(raw_input("Guess row: ")) - 1
            useless_var_row = board[guess_row]
            break
        except:
            print "\nThat location is unavailable. Please pick another row (from 1 to 5)."

    """ guess_row = int(raw_input("Guess Row: ")) - 1
        guess_col = int(raw_input("Guess Col: ")) - 1
    """
    enemy_guess_row = random_row(board)
    enemy_guess_col = random_col(board)
#THIS MAKES SURE THAT THE ENEMY IS SHOOTING IN A VALID LOCATION
    while True:
        if ((board[enemy_guess_row][enemy_guess_col] != "O") and (board[enemy_guess_row][enemy_guess_col] != "B")) \
        or (enemy_guess_col == guess_col and enemy_guess_row == guess_row):
            enemy_guess_row = random_row(board)
            enemy_guess_col = random_row(board)
        if ((board[enemy_guess_row][enemy_guess_col] == "O") or (board[enemy_guess_row][enemy_guess_col] == "B")) \
        and (enemy_guess_col != guess_col and enemy_guess_row != guess_row):
            board[enemy_guess_row][enemy_guess_col] = "Y"
            break
# THIS IS WHAT DETERMINES IF YOU WON OR NOT EACH ROUND
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sank the enemy's battleship!"
        break
#
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