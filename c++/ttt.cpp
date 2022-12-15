#include <stdio.h>
#include <time.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
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

string checkWin()
{
    // TODO: check for winner
    return "u";
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
    vector<int> allowedChoices = {};
    for (int i = 0; sizeof(board); i++)
    {
        if (board[i] == "*")
        {
            // allowedChoices.push_back(i);
        }
    }
}

int main()
{
    clear();
    cpuTurn();
    printBoard();
    return 0;
}