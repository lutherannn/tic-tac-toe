import random
import os
import sys


board = ["*", "*", "*", "*", "*", "*", "*", "*", "*"]
wins = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)
done = False


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def printBoard():
    print(
        " ".join(board[0:3]) + "\n" + " ".join(board[3:6]) + "\n" + " ".join(board[6:9])
    )


# I'm not proud of this, lol. but it's what i can figure out for now...
# Some nerd: uhm accccshually it's indices
def getIndexes(lst, item):
    r = []
    for x in lst:
        if x == item:
            r.append(lst.index(x))
            lst[lst.index(x)] = "A"
    for x in lst:
        if x == "A":
            lst[lst.index(x)] = "*"
    return r


def userTurn():
    validUserTurn = False
    while not validUserTurn:
        userChoice = int(input("Choose square to put your X: "))
        userChoice -= 1
        if userChoice in getIndexes(board, "*"):
            board[userChoice] = "X"
            validUserTurn = True
        else:
            print("Square already taken.")


def cpuTurn():
    board[random.choice(getIndexes(board, "*"))] = "O"


def checkWin(inBoard, player):
    return (
        (inBoard[0] == player and inBoard[1] == player and inBoard[2] == player)
        or (inBoard[3] == player and inBoard[4] == player and inBoard[5] == player)
        or (inBoard[6] == player and inBoard[7] == player and inBoard[8] == player)
        or (inBoard[0] == player and inBoard[3] == player and inBoard[6] == player)
        or (inBoard[1] == player and inBoard[4] == player and inBoard[7] == player)
        or (inBoard[2] == player and inBoard[5] == player and inBoard[8] == player)
        or (inBoard[0] == player and inBoard[4] == player and inBoard[8] == player)
        or (inBoard[2] == player and inBoard[4] == player and inBoard[6] == player)
    )


clear()
printBoard()
print(
    "Grid numbers are 1-9 with the upper left corner being 1, working from left to right."
)
userChoice = int(input("Choose square to put first X: "))
board[userChoice - 1] = "X"


while not done:
    cpuTurn()
    clear()
    printBoard()
    if checkWin(board, "O"):
        print("Cpu wins!")
        sys.exit(0)
    if "*" not in board:
        print("Draw!")
        sys.exit(0)
    userTurn()
    clear()
    printBoard()
    if checkWin(board, "X"):
        print("User wins!")
        sys.exit(0)
    if "*" not in board:
        print("Draw!")
        sys.exit(0)
