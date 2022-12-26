#include <stdio.h>
#include <time.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
using namespace std;

string board[] = {"*", "*", "*", "*", "*", "*", "*", "*", "*"};
vector<int> legalSquares;

void clear()
{
    system("cls");
}

void printBoard()
{
    int newlCounter = 0;
    for (int x = 0; x < sizeof(board) / sizeof(board[0]); x++)
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
    int userChoice;
    while (!validUserTurn)
    {
        cout << "Enter square to put your X: ";
        cin >> userChoice;
        userChoice--;
        if (board[userChoice] == "*")
        {
            board[userChoice] = "X";
            validUserTurn = true;
        }
        else
        {
            cout << "Square not valid or already taken";
        }
    }
}

void cpuTurn()
{
    bool validCpuTurn = false;
    getLegalSquares();
    srand(time(0));

    while (!validCpuTurn)
    {
        int cpuChoice = rand() % legalSquares.size();
        if (find(legalSquares.begin(), legalSquares.end(), cpuChoice) != legalSquares.end())
        {
            board[cpuChoice] = "O";
            validCpuTurn = true;
        }
    }

}

int main()
{
    // clear();
    userTurn();
    cpuTurn();
    printBoard();
    return 0;
}
