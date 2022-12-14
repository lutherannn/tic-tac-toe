import random
import os


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


board = ["*", "*", "*", "*", "*", "*", "*", "*", "*"]
done = False

clear()
printBoard()
print(
    "Grid numbers are 1-9 with the upper left corner being 1, working from left to right."
)
userChoice = int(input("Choose square to put first X: "))
board[userChoice - 1] = "X"

for _ in range(5):
    cpuTurn()
    clear()
    printBoard()
    userTurn()
    clear()
    printBoard()
