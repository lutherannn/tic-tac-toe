import random
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def printBoard():
    print(
        " ".join(board[0:3]) + "\n" + " ".join(board[3:6]) + "\n" + " ".join(board[6:9])
    )


# This doesn't work, idk why. it's 4:30 in the morning and i cba to figure it out. never enters the if statement.
def cpuTurn():
    validCpuChoice = False
    while not validCpuChoice:
        cpuChoice = random.randrange(0, 9)
        if board[cpuChoice] == "*":
            board[cpuChoice] = "O"
            validCpuChoice = True
            break


clear()
board = ["*", "*", "*", "*", "*", "*", "*", "*", "*"]
done = False

printBoard()
print(
    "Grid numbers are 1-9 with the upper left corner being 1, working from left to right."
)
userChoice = int(input("Choose square to put first X: "))
board[userChoice - 1] = "X"
printBoard()

# while not done:
for _ in range(10):
    cpuTurn()
    done = True
