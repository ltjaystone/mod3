def printBoard(board):
    print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("-----------")
    print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("-----------")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])

def checkWinner(board, letter):
    if board[0][0] == letter and board[0][1] == letter and board[0][2] == letter:
        return True
    if board[1][0] == letter and board[1][1] == letter and board[1][2] == letter:
        return True
    if board[2][0] == letter and board[2][1] == letter and board[2][2] == letter:
        return True
    if board[0][0] == letter and board[1][0] == letter and board[2][0] == letter:
        return True
    if board[0][1] == letter and board[1][1] == letter and board[2][1] == letter:
        return True
    if board[0][2] == letter and board[1][2] == letter and board[2][2] == letter:
        return True
    if board[0][0] == letter and board[1][1] == letter and board[2][2] == letter:
        return True
    if board[0][2] == letter and board[1][1] == letter and board[2][0] == letter:
        return True

def changeTurn(letter):
    if letter == "x":
        letter = "o"
    else:
 
        letter = "x"
    return letter

count = 0
letter = "x"


