import copy, sys, random
import games.connectfour.CheckWin as CheckWin

turns = ['red', 'yellow']

def ChooseRandomMove(board):
    possibleMoves = []
    for i in range(7):
        if board[0][i] == ' ':
            possibleMoves.append(i)
    
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else: return False

def DoubleCheck(board, move, turn):
    for row in range(5, -1, -1):
        deepCopy = copy.deepcopy(board)
        if deepCopy[row][move] == ' ':
            deepCopy[row][move] = turns[turn]
            if row-1 >= 0: deepCopy[row-1][move] = turns[0 if turn == 1 else 1]
            else: return False
            if CheckWin(deepCopy, 0 if turn == 1 else 0):
                return True
            else:
                return False

def GetComputerMove(board, turn):
    for i in range(7):
        copyBoard = copy.deepcopy(board)
        for row in range(5, -1, -1):
            copyBoard = copy.deepcopy(board)
            if copyBoard[row][i] == ' ':
                copyBoard[row][i] = turns[turn]
                if CheckWin(copyBoard, turn):
                    return i
    
    for i in range(7):
        copyBoard = copy.deepcopy(board)
        for row in range(5, -1, -1):
            copyBoard = copy.deepcopy(board)
            if copyBoard[row][i] == ' ':
                copyBoard[row][i] = turns[0 if turn == 1 else 1]
                if CheckWin(copyBoard, 0 if turn == 1 else 0):
                    if DoubleCheck(copy.deepcopy(board), i, 0 if turn == 1 else 0):
                        return i
    
    copyBoard = copy.deepcopy(board)
    move = ChooseRandomMove(copyBoard)
    if type(move) == int:
        while DoubleCheck(copyBoard, move, turn):
            move = ChooseRandomMove(copyBoard)
        return move
    else: return False

sys.modules[__name__] = GetComputerMove