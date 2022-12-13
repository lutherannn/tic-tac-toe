#include <stdio.h>
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
    // TODO: process user turn
}

void cpuTurn()
{
    // TODO: process CPU turn
}

int main()
{
    printBoard();
    return 0;
}