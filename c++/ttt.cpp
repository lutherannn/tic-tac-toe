#include <stdio.h>
#include <time.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
using namespace std;

string board[] = {"*", "*", "*", "*", "*", "*", "*", "*", "*"};
vector<int> legalSquares = {};

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

void getLegalSquares()
{
    for (int i = 0; i < sizeof(board) / sizeof(board[0]); i++)
    {
        if (board[i] == "*")
        {
            legalSquares.push_back(i);
        }
    }
}

void userTurn()
{
    bool validUserTurn = false;
    getLegalSquares();
    while (!validUserTurn)
    {
    }
}

void cpuTurn()
{
    bool validCpuTurn = false;
    getLegalSquares();
    while (!validCpuTurn)
    {
        srand(time(0));
        int cpuChoice = rand() % legalSquares.size();
        if (find(legalSquares.begin(), legalSquares.end(), cpuChoice) != legalSquares.end())
        {
            board[cpuChoice] = "O";
            validCpuTurn = true;
        }
        else
        {
            cout << "fuck.";
        }
    }
}

int main()
{
    clear();
    printBoard();
    clear();
    return 0;
}