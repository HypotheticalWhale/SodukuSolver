from pip import main

def isInRow(Board,number,row):
    for i in range(9):
        if Board[row][i] == number:
            return True
    return False

def isInColumn(Board,number,column):
    for i in range(9):
        if Board[i][column] == number:
            return True
    return False

def isInBox(Board,number,row,column):
    localRow  = row - (row % 3)
    localColumn = column - (column % 3)
    for i in range(localRow, localRow + 3):
        for j in range(localColumn,localColumn +3):
         if Board == number:
             return True
    return False

def isValidPos(Board,number,row,column):
    valid = not isInRow(Board,number,row) and not isInColumn(Board,number,column) and not isInBox(Board,number,row,column)
    return valid

def solveBoard(Board):
    for i in range(9):
        for j in range(9):
            if Board[i][j] == 0:
                for k in range(1,10):
                    if isValidPos(Board,k,i,j):
                        Board[i][j] = k
                        if solveBoard(Board):
                            return True
                        else:
                            Board[i][j] = 0
                return False
    return True

def printBoard(board):
    for i in range(9):
        if i != 0: 
            print("|",end = "")
            print()
        if i % 3 == 0:
            print("-------------")
        for j in range(9):
            if j % 3 == 0:
                print("|",end = "")
            print(board[i][j],end = "")
    print("|")
    print("-------------")
    
if __name__ == '__main__':
    board = [[7,3,2,1,5,0,6,0,0],
             [0,0,0,0,0,3,0,0,0],
             [1,0,0,0,0,9,5,0,0],
             [8,0,0,0,0,0,0,9,0],
             [0,4,3,0,0,0,7,5,0],
             [0,9,0,0,0,0,0,0,8],
             [0,0,9,7,0,0,0,0,5],
             [0,0,0,2,0,0,0,0,0],
             [0,0,7,0,4,0,2,0,3]]
    printBoard(board)
    if(solveBoard(board)):
        print("Solved!!:")
        printBoard(board)
    else:
        print("Cannot be solved")