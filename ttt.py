board = []

for i in range(3):
    temp = []
    for j in range(3):
        temp.append("  ")
    board.append(temp)

count = 0
letter = "x"

while count < 9 and count >= 0:

    print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print(" -------- ")
    print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print(" -------- ")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])

    x = int(input("pls enter the x coordinate of your piece "))
    y = int(input("pld enter the y coordinate of your piece"))

    board[x][y] = letter

    count += 1

    if board[0][0] == letter and board[0][1] == letter and board[0][2] == letter:
        print(letter, "wins")
        count = -1
    
    if board[1][0] == letter and board[1][1] == letter and board[1][2] == letter:
        print(letter, "wins")
        count = -1
    
    if board[2][0] == letter and board[2][1] == letter and board[2][2] == letter:
        print(letter, "wins")
        count = -1
    
    if board[0][0] == letter and board[1][0] == letter and board[2][0] == letter:
        print(letter, "wins")
        count = -1

