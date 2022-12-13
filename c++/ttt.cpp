#include <stdio.h>
#include <time.h>
#include <iostream>
using namespace std;

string board[] = {"*", "*", "*", "*", "*", "*", "*", "*", "*"};

void clear()
{
    system("cls");
}

void printBoard()
{
    int newlCounter = 0;
    for (int x = 0; x <= sizeof(board); x++)
    {
        newlCounter++;
        cout << board[x];
        if (newlCounter == 3)
        {
            cout << endl;
            newlCounter = 0;
        }
    }
}

bool checkWin()
{
    // TODO: check for winner
    return true;
}

void userTurn()
{
    bool validUserTurn = false;
    while (!validUserTurn)
    {
    }
}

void cpuTurn()
{
    bool validCpuTurn = false;
    while (!validCpuTurn)
    {
        int cpuChoice = rand() % 10;
        if (cpuChoice == 0)
        {
            board[0] = "O";
            validCpuTurn = true;
        }
        if (board[cpuChoice - 1] == "*")
        {
            board[cpuChoice - 1] = "O";
            validCpuTurn = true;
        }
    }
    validCpuTurn = false;
}

int main()
{
    srand(time(0));
    clear();
    cpuTurn();
    printBoard();
    return 0;
}