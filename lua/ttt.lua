-- why does lua indexing start at 1? who knows but it makes this less confusing at least.
local board = {"*", "*", "*", "*", "*", "*", "*", "*", "*"}
local legalSquares = {}
local validChoice = false

local function clear()
    local ok, err, code = os.rename("C:\\Windows", "C:\\Windows")
    if not ok then
        if code == 13 then
            os.execute("cls")
        end
    else
        os.execute("clear")
    end
    os.execute("cls")
end

local function printBoard()
    local newlCounter = 0
    for i = 1, #board do
        io.write(board[i])
        newlCounter = newlCounter + 1

        if newlCounter == 3 then
            io.write("\n")
            newlCounter = 0
        end
    end
end

local function userTurn()
    while validChoice == false do
        io.write("Choose a square to put your X: ")
        local userChoice = io.read("*n")

        if board[userChoice] == "*" then
            board[userChoice] = "X"
            validChoice = true
        else
            print("Square not valid or already taken.")
        end
    end
    validChoice = false
end

local function cpuTurn()
    while validChoice == false do
        local cpuChoice = math.random(#board)
        if board[cpuChoice] == "*" then
            board[cpuChoice] = "O"
            validChoice = true
        end
    end
    validChoice = false
end

local function checkWin()
    local filledSpaces = 0
    if board[1] == "X" and board[2] == "X" and board[3] == "X" then
        return "u"
    end
    if board[4] == "X" and board[5] == "X" and board[6] == "X" then
        return "u"
    end
    if board[7] == "X" and board[8] == "X" and board[9] == "X" then
        return "u"
    end
    if board[1] == "X" and board[4] == "X" and board[7] == "X" then
        return "u"
    end
    if board[2] == "X" and board[5] == "X" and board[8] == "X" then
        return "u"
    end
    if board[3] == "X" and board[6] == "X" and board[9] == "X" then
        return "u"
    end
    if board[1] == "X" and board[5] == "X" and board[9] == "X" then
        return "u"
    end
    if board[3] == "X" and board[5] == "X" and board[7] == "X" then
        return "u"
    end

    if board[1] == "O" and board[2] == "O" and board[3] == "O" then
        return "c"
    end
    if board[4] == "O" and board[5] == "O" and board[6] == "O" then
        return "c"
    end
    if board[7] == "O" and board[8] == "O" and board[9] == "O" then
        return "c"
    end
    if board[1] == "O" and board[4] == "O" and board[7] == "O" then
        return "c"
    end
    if board[2] == "O" and board[5] == "O" and board[8] == "O" then
        return "c"
    end
    if board[3] == "O" and board[6] == "O" and board[9] == "O" then
        return "c"
    end
    if board[1] == "O" and board[5] == "O" and board[9] == "O" then
        return "c"
    end
    if board[3] == "O" and board[5] == "O" and board[7] == "O" then
        return "c"
    end
    --so i didn't realize this was broke as hell lmao, but this soltuion will work in the meantime
    for i = 1, #board do
        if board[i] ~= "*" then
            filledSpaces = filledSpaces + 1
        end
        if filledSpaces == 9 then
            return "d"
        end
    end
end

while true do
    clear()
    printBoard()
    userTurn()
    clear()
    printBoard()
    if checkWin() == "u" then
        print("You win!")
        os.exit()
    end
    if checkWin() == "d" then
        print("Tie!")
        os.exit()
    end
    cpuTurn()
    clear()
    printBoard()
    if checkWin() == "c" then
        print("CPU wins!")
        os.exit()
    end
    if checkWin() == "d" then
        print("Tie!")
        os.exit()
    end
end
