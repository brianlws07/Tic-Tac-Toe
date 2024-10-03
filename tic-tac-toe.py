#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#

# import libraries
import unittest

# The Game Board 
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# TODO: update the gameboard with the user input
def markBoard(position, mark):
    board[int(position)] = mark

# TODO: print the game board as described at the top of this code skeleton
# Will not be tested in Part 1
def printBoard():
    print("\n")
    for i in range(1, len(board)+1, 3): #1, 4, 7
        output = []
        for j in range(i, i + 3):
            if board[j] != ' ':
                output.append(board[j])
            else:
                output.append(str(j))
        output = " | ".join(output)
        print(" " + output)
        if i < 7:
            print(" ---------")
    print("\n")


# TODO: check for wrong input, this function should return True or False.
# True denoting that the user input is correct
# you will need to check for wrong input (user is entering invalid position) or position is out of bound
# another case is that the position is already occupied
def validateMove(position):
    try:
        position = position
        pos = int(position)
        if pos < 1 or pos > 9:
            return False
        elif board[pos] != " ":
          return False
        else:
            return True
    except (ValueError, KeyError):
        return False
    
    
# TODO: list out all the combinations of winning, you will neeed this
# one of the winning combinations is already done for you
winCombinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 5, 9],
    [3, 5, 7],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

# TODO: implement a logic to check if the previous winner just win
# This method should return with True or False
def checkWin(player):
    player_coordinate = []
    for k, v in board.items():
        if v == player:
            player_coordinate.append(k)
    for wins in winCombinations:
        if all(pos in player_coordinate for pos in wins):
            return True
    
    return False
        

# TODO: implement a function to check if the game board is already full
# For tic-tac-toe, tie bascially means the whole board is already occupied
# This function should return with boolean
def checkFull():
    if all(board[k] != " " for k in board):
        return True
    
    return False

def restartBoard(board):
    for pos in board:
            board[pos] = ' '

def askForRestart():
    return input("Would you like to restart the game (Y/N): ").lower().startswith('y')

#########################################################
## Copy all your code/fucntions in Part 1 to above lines
## (Without Test Cases)
#########################################################

gameEnded = False
currentTurnPlayer = 'X'

# entry point of the whole program
print('Game started: \n\n' +
    ' 1 | 2 | 3 \n' +
    ' --------- \n' +
    ' 4 | 5 | 6 \n' +
    ' --------- \n' +
    ' 7 | 8 | 9 \n')

# TODO: Complete the game play logic below
# You could reference the following flow
# 1. Ask for user input and validate the input
# 2. Update the board
# 3. Check win or tie situation
# 4. Switch User
while not gameEnded:
    move = input(currentTurnPlayer + "'s turn, input: ").strip("'\"")
    while not validateMove(move):
        print("Invalid move, please reenter input")
        move = input(currentTurnPlayer + "'s turn, input: ")

    markBoard(move, currentTurnPlayer)
    printBoard()

    if checkWin(currentTurnPlayer):
        print(f"Congrats! {currentTurnPlayer} has won!")
        if askForRestart():
            restartBoard(board)
            currentTurnPlayer = 'X'
            printBoard()
            continue
        else:
            gameEnded = True
    elif checkFull():
        print("It is a draw!")
        if askForRestart():
            restartBoard(board)
            currentTurnPlayer = 'X'
            printBoard()
            continue
        else:
            gameEnded = True

    currentTurnPlayer = 'O' if currentTurnPlayer == 'X' else 'X'

print("Game Over. Thanks for playing!")

# Bonus Point: Implement the feature for the user to restart the game after a tie or game over
