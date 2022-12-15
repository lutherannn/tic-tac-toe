$board = ["*", "*", "*", "*", "*", "*", "*", "*", "*"]
$legalSquares = []
$validChoice = false

def clear
    system("clear") || system("cls")    
end

def printBoard()
    newlCounter = 0
    for x in 0..8 do
        print($board[x])
        newlCounter = newlCounter + 1
        
        if newlCounter == 3 then
            print("\n")
            newlCounter = 0
        end
    end
    STDOUT.flush()
end

def getIndexes()
    for x in $board do
        if x == "*" then
            $legalSquares.push($board.index(x))
            $board[$board.index(x)] = "A"
        end
    end
    for x in $board do
        if x == "A" then
            $board[$board.index(x)] = "*"
        end
    end
end

def userTurn()
    getIndexes()
    while $validChoice == false do
        print("Choose a square you put your X: ")
        userChoice = gets.chomp().to_i() - 1
        if $legalSquares.include?(userChoice) then
            $board[userChoice] = "X"
            $validChoice = true
        else
            puts("Square not valid or already taken")
        end
    end
    $validChoice = false
end

def cpuTurn()
    getIndexes()
    $board[$legalSquares.sample()] = "O"
end

clear()
userTurn()
printBoard()
clear()
cpuTurn()
printBoard()