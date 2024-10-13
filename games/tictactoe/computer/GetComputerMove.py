import sys
import random
import copy
import games.tictactoe.CheckWin as CheckWin

turns = ['X', 'O']

def ChooseRandomMove(board, moveList):
    possibleMoves = []
    for i in moveList:
        if board[i[0]][i[1]] == '?':
            possibleMoves.append(i)
    
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else: return False

def GetComputerMove(board):

    for i in range(3):
        copyBoard = copy.deepcopy(board)
        for j in range(3):
            copyBoard = copy.deepcopy(board)
            if copyBoard[i][j] == '?':
                copyBoard[i][j] = turns[1]
                if CheckWin(copyBoard, turns[1]):
                    return [i,j]
    
    for i in range(3):
        copyBoard = copy.deepcopy(board)
        for j in range(3):
            copyBoard = copy.deepcopy(board)
            if copyBoard[i][j] == '?':
                copyBoard[i][j] = turns[0]
                if CheckWin(copyBoard, turns[0]):
                    return [i,j]
    
    move = ChooseRandomMove(board, [[0,0],[0,2],[2,0],[2,2]])
    if move != False:
        return move
    
    if board[1,1] == '?':
        return [1,1]

sys.modules[__name__] = GetComputerMove