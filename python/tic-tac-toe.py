import random
import os
import sys


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
        if userChoice - 1 in getIndexes(board, "*"):
            board[userChoice - 1] = "X"
            validUserTurn = True
        else:
            print("Square already taken.")


def cpuTurn():
    board[random.choice(getIndexes(board, "*"))] = "O"


def checkWin():
    if "".join(board[0:3]) == "XXX":
        return "u"
    if "".join(board[3:6]) == "XXX":
        return "u"
    if "".join(board[6:9]) == "XXX":
        return "u"
    if board[0] == "X" and board[4] == "X" and board[8] == "X":
        return "u"
    if board[2] == "X" and board[4] == "X" and board[6] == "X":
        return "u"
    if board[1] == "X" and board[4] == "X" and board[7] == "X":
        return "u"
    if board[0] == "X" and board[3] == "X" and board[6] == "X":
        return "u"
    if board[2] == "X" and board[5] == "X" and board[8] == "X":
        return "u"
    if "".join(board[0:3]) == "OOO":
        return "c"
    if "".join(board[3:6]) == "OOO":
        return "c"
    if "".join(board[6:9]) == "OOO":
        return "c"
    if board[0] == "O" and board[4] == "O" and board[8] == "O":
        return "c"
    if board[2] == "O" and board[4] == "O" and board[6] == "O":
        return "c"
    if board[1] == "O" and board[4] == "O" and board[7] == "O":
        return "c"
    if board[0] == "O" and board[3] == "O" and board[6] == "O":
        return "c"
    if board[2] == "O" and board[5] == "O" and board[8] == "O":
        return "c"
    if "*" not in board:
        return "d"


board = ["*", "*", "*", "*", "*", "*", "*", "*", "*"]
done = False

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
    if checkWin() == "c":
        print("CPU Wins")
        sys.exit()
    if checkWin() == "d":
        print("Tie!")
        sys.exit()
    userTurn()
    clear()
    printBoard()
    if checkWin() == "u":
        print("You win!")
        sys.exit()
    if checkWin() == "d":
        print("Tie!")
        sys.exit()
